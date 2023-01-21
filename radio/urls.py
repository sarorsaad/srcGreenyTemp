from django.urls import path
from . import views
from .views import dashboard
from .views import physician_portal
from .views import receptionist_portal
from .views import appointment_booking
from .views import consents


app_name='radio'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('physician-portal/', physician_portal, name='physician'),
    path('receptionist_portal/', receptionist_portal, name='receptionist'),
    path('appointment_booking/', appointment_booking, name='appointment_booking'),
    path('reports/', views.reports, name='reports'),
    path('consents/', consents, name='consents'),
   
   
]
