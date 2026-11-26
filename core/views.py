from django.shortcuts import render
from . import views
def home(request):
    hospitals={
        'name':'CAREWELL',
        'location':'RAMANATTULARA,KOZHIKODE',
        'phone number':'9083838292'
    }
    return render(request,'home.html',{'hospital':hospitals})
