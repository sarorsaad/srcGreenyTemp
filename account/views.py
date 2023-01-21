from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'registration/profile.html')


def register_view(request):
    return render(request, 'registration/register.html')
 

def login_view(request):
    return render(request, 'registration/login.html')
    

def reset_password_view(request):
    return render(request, 'registration/reset_password.html')

def change_password(request):
    return render(request, 'registration/change_password.html')

def edit_profile(request):
    return render(request, 'registration/edit_profile.html')

def add_contact(request):
    return render(request, 'registration/add_contact.html')

def edit_contact(request):
    return render(request, 'registration/edit_contact.html')