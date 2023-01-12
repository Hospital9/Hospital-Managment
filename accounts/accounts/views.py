from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail

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
			last_name = form.cleaned_data.get('last_name')
			
			group = Group.objects.get(name=last_name)
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
		us1=User.objects.get(username=username)
		group = Group.objects.get(name=us1.last_name)

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if group == 'doctors':
				return redirect('Doctor_homepage')
			if group == 'patents':
				return redirect('Patient_homepage')
			if group == 'nurses':
				return redirect('Nurse_homepage')	
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
def Doctor_homepage(request):



	context = {}
	return render(request,'accounts/Doctor_homepage.html',context)


@login_required(login_url='login')
def Appointments(request):
	'''
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		send_mail(message_name,message,message_email,receiver_email,)
		return render(request,'accounts/Appointments.html')
	else:
		'''
	return render(request,'accounts/patient.html')

@login_required(login_url='login')
@patient_only
@doctor_only
def Patient_homepage(request, pk):
	patient = Patient.objects.get(id=pk)
	return render(request,'accounts/Patient_homepage.html')

@login_required(login_url='login')
@nurse_only
def Nurse_homepage(request):
    return render(request,'accounts/Nurse.html')

@login_required(login_url='login')
def BloodTests(request):
    return render(request,'accounts/BloodTests.html')

@login_required(login_url='login')
def contact(request):
	'''
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		send_mail(message_name,message,message_email,['rashedamar27@gmail.com'],)

		return render(request,'accounts/contact.html', {'message-name':message_name})

    else:
    	'''
	return render(request,'accounts/contact.html')

@login_required(login_url='login')
@doctor_only
def patient_list(request):
	patient_list = Patient.objects.all()
	

	context = {'patient_list':patient_list}
	return render(request,'accounts/patient_list.html',context)