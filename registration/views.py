from home import forms
from django.shortcuts import render
from django.http import HttpRequest
from .forms import SineUpForm
from django.contrib import messages
# Create your views here.
def profile(request):
    return render(request, 'registration/profile.html')

def register(request):
    if request.method == "POST":
        fm = SineUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SineUpForm()
    return render(request, 'registration/register.html', {'form': fm})