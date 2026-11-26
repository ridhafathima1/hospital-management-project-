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
def departments(request):
    departmentslist={
        'department1':'cardiology',
        'department2':'neurology',
        'department3':'orthopedics',
    }
    return render(request,'department.html',{'department':departmentslist})
