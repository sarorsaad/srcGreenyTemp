from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_view(request):
        return render(request, 'radio/index.html')

def register_view(request):
        return render(request, 'radio/register.html')
   

@login_required
def login_view(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # invalid login
                pass
        return render(request, 'radio/login.html')