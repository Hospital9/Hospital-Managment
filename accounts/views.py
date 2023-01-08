from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#create your views here
from .models import *
from .forms import CreateUserForm

# Create your views here.
from .decorators import unauthenticated_user, allowed_users, doctor_only, nurse_only, patient_only


@unauthenticated_user
def registerpage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='patient')
			user.groups.add(group)

			messages.success(request,'Account was created for ' + username)


			return redirect('login')

	context = {'form':form}
	return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginpage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'username or password is incorrect')

	context = {}
	return render(request,'accounts/login.html',context)

def logoutuser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request,'accounts/dashboard.html')

@login_required(login_url='login')
@doctor_only
def doctors(request):
    return render(request,'accounts/doctors.html')

@login_required(login_url='login')
def Appointments(request):
    return render(request,'accounts/Appointments.html')

@login_required(login_url='login')
@patient_only
def Patient(request):
	return render(request,'accounts/Patient.html')

@login_required(login_url='login')
@nurse_only
def Nurse(request):
    return render(request,'accounts/Nurse.html')

@login_required(login_url='login')
def BloodTests(request):
    return render(request,'accounts/BloodTests.html')