from django.db import models

# Create your models here.

class Doctor(models.Model):
	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=10,null=True)
	password = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.name


class Nurse(models.Model):
	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=10,null=True)
	password = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name


class Patient(models.Model):

	Doctor	= models.ForeignKey(Doctor,null=True,on_delete= models.SET_NULL)

	name = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=10,null=True)
	password = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.name


class BloodTest(models.Model):
	
	Nurse = models.ForeignKey(Nurse,null=True,on_delete= models.SET_NULL)
	Patient	= models.ForeignKey(Patient,null=True,on_delete= models.SET_NULL)

	BloodTyping = models.CharField(max_length=200,null=True)
	BloodCholestero = models.CharField(max_length=200,null=True)
	BloodGasesTest = models.CharField(max_length=200,null=True)
	BloodGlucose = models.CharField(max_length=200,null=True)