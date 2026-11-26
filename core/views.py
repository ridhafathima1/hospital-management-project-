from django.shortcuts import render
def home(request):
    hospitals={
        'name':'CAREWELL',
        'location':'RAMANATTUKARA KOZHIKODE',
        'phone number':'234567899'
    }
    return render(request,'home.html',{'hospitals':hospitals})