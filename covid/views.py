from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "78c5a77459msh4f149f5ef9f90e4p12113fjsnaa290edcffcc",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


def country(request):
    noofresults=int(response['results'])
    list1=[]
    for x in range(0,noofresults):
        list1.append(response['response'][x]['country'])
    if request.method=='POST':
        selectedcountry=request.POST['selectedcountry']
        noofresults=int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'selectedcountry':selectedcountry,'list1':list1,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'covid/hello.html',context)    
    
    context={'list1':list1}
    return render(request,'covid/hello.html',context)