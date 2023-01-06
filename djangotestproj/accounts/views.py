from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#create your views here
from .forms import CreateUserForm

# Create your views here.
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def registerpage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for ' + user)


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
@allowed_users(allowed_roles=['doctors'])
def doctors(request):
    return render(request,'accounts/doctors.html')

@login_required(login_url='login')
def Appointments(request):
    return render(request,'accounts/Appointments.html')

@login_required(login_url='login')
def Patient(request):
	#patient = Patient.objects.all()

    return render(request,'accounts/Patient.html')

@login_required(login_url='login')
def Nurse(request):
    return render(request,'accounts/Nurse.html')

@login_required(login_url='login')
def BloodTests(request):
    return render(request,'accounts/BloodTests.html')

@login_required(login_url='login')
def Contact(request):
    return render(request,'accounts/contact.html')