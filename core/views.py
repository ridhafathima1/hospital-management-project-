from django.shortcuts import render,redirect
from .forms import Registrationform
from django.contrib.auth import authenticate,login,logout
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
def register(request):
    if request.method=='POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=Registrationform()
    return render(request,'register.html',{'form':form}) 
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'invalid email or password'})
    return render(request,'login.html')
