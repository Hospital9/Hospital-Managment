from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

class BloodTestForm(ModelForm):
	class Meta:
		model = BloodTest
		fields = '__all__'

class AppointmentsForm(ModelForm):
	class Meta:
		model = Appointments
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','last_name','email','password1','password2']
