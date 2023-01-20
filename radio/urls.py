from django.urls import path
from . import views


app_name='radio'

urlpatterns = [
    path('index/', views.home_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
   
]
