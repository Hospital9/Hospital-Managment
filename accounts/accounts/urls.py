from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),


    path('', views.home, name="home"),
    path('Doctor_homepage/',views.Doctor_homepage, name="Doctor_homepage"),
    path('Patient_homepage/',views.Patient_homepage, name="Patient_homepage"),
    path('Nurse_homepage/',views.Nurse_homepage, name="Nurse_homepage"),
    path('BloodTests/',views.BloodTests, name="BloodTests"),
    path('Appointments/',views.Appointments, name="Appointments"),
    path('contact/',views.contact, name="contact"),
    path('patient_list/',views.patient_list, name="patient_list"),

]

