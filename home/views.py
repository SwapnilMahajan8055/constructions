from django.shortcuts import render
from django.http import HttpRequest
from .forms import StudentRegistration 
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request, 'home/home.html')
def about(request):
    return render(request, 'home/about.html')  
def clients(request):
    return render (request,'home/clients.html')
def service(request):
    return render (request,'home/services.html')
def banner(request):
    return render (request,'home/banner.html')
def plan(request):
    return render (request,'home/plan.html')
def model(request):
    return render (request,'home/model.html')
def contact(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your Data Has Been Submited........')
    else:
        fm = StudentRegistration()
    return render(request, 'home/contact.html' , {'form':fm})
def logabout(request):
    return render(request, 'home/logabout.html')  
