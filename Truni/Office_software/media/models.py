from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login,logout,authenticate
# Create your models here.



class NameAbstract(models.Model):
	# abstract model
	name = models.CharField(max_length=61)
	class Meta:
		abstract = True

class Registration(AbstractUser):
	fathername =  models.CharField(max_length=250)
	dob = models.CharField(max_length=250)
	spouse_name =  models.CharField(max_length=250)
	married_anv =  models.CharField(max_length=250)
	current_add =  models.CharField(max_length=250)
	personal_contactno =  models.IntegerField(blank=True)
	emergencyno = models.IntegerField(blank=True)
	highest_education = models.CharField(max_length=250)
	education_instituename = models.CharField(max_length=250)
	year_passing = models.CharField(max_length=250)
	firstemployee_name = models.CharField(max_length=250)
	employee_from = models.CharField(max_length=250)
	employee_to = models.DateField()
	photo_id = models.FileField(blank=True, null=True)
	pan_no = models.CharField(max_length=250)
	bank_accountno = models.IntegerField(blank=True)
	bank_branch = models.CharField(max_length=250)
	bank_ifsccode = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	Image = models.FileField(blank=True, null=True)
	Jdate = models.CharField(max_length=250)
	sex = models.CharField(max_length=250)


