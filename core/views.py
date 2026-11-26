from django.shortcuts import render
from . import views
def home(request):
    hospitals={
        'name':'CAREWELL',
        'location':'RAMANATTULARA,KOZHIKODE',
        'phonenumber':'9083838292'
    }
    return render(request,'home.html',{'hospital':hospitals})
def doctors(request):
    doctorslist=['dr.ridha fathima','dr.raniya','dr.rayan']
    return render(request,'doctors.html',{'doctor':doctorslist})
