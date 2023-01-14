from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver
# Create your models here.


class Patient(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=10,null=True)
	password = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.name


class BloodTest(models.Model):
	Patient	= models.ForeignKey(Patient,null=True,on_delete= models.SET_NULL)

	BloodTyping = models.CharField(max_length=200,null=True)
	BloodCholestero = models.CharField(max_length=200,null=True)
	BloodGasesTest = models.CharField(max_length=200,null=True)
	BloodGlucose = models.CharField(max_length=200,null=True)
	notes = models.CharField(max_length=200,null=True)



class Appointments(models.Model):
	Patient	= models.ForeignKey(Patient,null=True,on_delete= models.SET_NULL)


	DATE = (
		)
	TIME = (
		)

	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	date = models.CharField(max_length=200,null=True,choices=DATE)
	time = models.CharField(max_length=200,null=True,choices=TIME)
	date_created = models.DateTimeField(auto_now_add=True,null=True)