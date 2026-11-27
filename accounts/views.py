from django.shortcuts import render,redirect
from .forms import Registrationform
def register(request):
    if request.method=='POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=Registrationform()
    return render(request,'register.html',{'form':form})    