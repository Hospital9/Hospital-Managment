from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),


    path('', views.home, name="home"),
    path('BloodTests/',views.BloodTests, name="BloodTests"),
    path('Appointments/',views.Appointments, name="Appointments"),
    path('contact/',views.contact, name="contact"),
    path('patient_list/',views.patient_list, name="patient_list"),
    path('Mail/',views.Mail, name="Mail"),
    path('add_patient/',views.add_patient, name="add_patient"),


]

