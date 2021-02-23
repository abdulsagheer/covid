from django.urls import path
from .views import country


app_name='cov'

urlpatterns = [
    path('',country,name="country")
]