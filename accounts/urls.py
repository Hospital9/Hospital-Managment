from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),


    path('', views.home, name="home"),
    #path('doctors/',views.doctors, name="doctors"),
    #path('Patient/',views.Patient, name="Patient"),
    #path('Nurse/',views.Nurse, name="Nurse"),
    #path('BloodTests/',views.BloodTests, name="BloodTests"),
    #path('Appointments/',views.Appointments, name="Appointments"),
]

