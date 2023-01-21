from django.urls import path
from .views import profile
from . import views
from .views import edit_profile



app_name='account'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
]
