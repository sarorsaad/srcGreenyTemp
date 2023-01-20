from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

def home_view(request):
        return render(request, 'radio/index.html')

def register_view(request):
        return render(request, 'radio/register.html')
   

       

def login_view(request):
        return render(request, 'radio/login.html')
        

def reset_password_view(request):
        return render(request, 'radio/reset_password.html')