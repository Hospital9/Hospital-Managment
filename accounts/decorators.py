from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request,*args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request,*args, **kwargs):

			group = None
			if request.user.groups.exists():
				group=request.user.groups.all()[0].name

			if group in allowed_roles:		
				return view_func(request,*args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator


def patient_only(view_func):
	def wrapper_function(request,*args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[2].name

		if group == 'doctors':
			return redirect('doctors')

		if group == 'nurses':
			return redirect('Nurse')

		if group == 'patients':
			return view_func(request,*args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function	


def nurse_only(view_func):
	def wrapper_function(request,*args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[1].name

		if group == 'patients':
			return redirect('Patient')

		if group == 'doctors':
			return redirect('doctors')

		if group == 'nurses':
			return view_func(request,*args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function	


def doctor_only(view_func):
	def wrapper_function(request,*args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'patients':
			return redirect('Patient')

		if group == 'nurses':
			return redirect('Nurse')

		if group == 'doctors':
			return view_func(request,*args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function	