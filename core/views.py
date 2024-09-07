from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'core/index.html', {'request': request})

def contact(request):
    
    return render(request, 'core/contact.html')