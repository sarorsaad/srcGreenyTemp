from django.shortcuts import render , redirect

from .models import Profile , UserPersonal_info , UserBio_info

from django.contrib.auth.models import User





# Create your views here.
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    personal_info = UserPersonal_info.objects.filter(user=profile.user)
    bio_info = UserBio_info.objects.filter(user=profile.user)
    if personal_info.exists():
       print(personal_info.values())
    else:
       print('No personal_info data found.')

    if bio_info.exists():
       print(bio_info.values())
    else:
       print('No bio_info data found.')


    return render(request, 'registration/profile.html',{'profile':profile , 
    'personal_info':personal_info ,'bio_info':bio_info })



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