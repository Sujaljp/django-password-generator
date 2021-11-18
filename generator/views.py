from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def eggs(request):
    return HttpResponse('<h1>I dont eat eggs<h1>')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    length = int(request.GET.get('length',12))
    thePassword = ''

    lowercase = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specail = list('!@#$%^&*')
    
    if request.GET.get('uppercase'):
        lowercase += uppercase
    if request.GET.get('numbers'):
        lowercase += numbers
    if request.GET.get('special'):
        lowercase += specail
    for i in range(length):
        thePassword += random.choice(lowercase)
    return render(request,'generator\password.html', {'password' : thePassword})