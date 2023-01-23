from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

def home_view(request):
        return render(request, 'radio/index.html')


def dashboard(request):
        # Code to handle the request and generate the response goes here
        return render(request, 'radio/dashboard.html')


def physician_portal(request):
        # Code to handle the request and generate the response goes here
        return render(request, 'radio/physician_portal.html')
        
def receptionist_portal(request):
        # Code to handle the request and generate the response goes here
        return render(request, 'radio/receptionist_portal.html')       
 
def appointment_booking(request):
        return render(request, 'radio/appointment_booking.html')

def reports(request):
        return render(request, 'radio/reports.html')

def consents(request):
        return render(request, 'radio/consents.html')

def technicians_portal(request):
        return render(request, 'radio/technicians_portal.html')

def radiologist_portal(request):
    return render(request, 'radio/radiologist_portal.html')
    