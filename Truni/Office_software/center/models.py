from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login,logout,authenticate


# Create your models here.
class RequestTracker(models.Model):
    client_ip = models.CharField(max_length=250, blank=True,null=True)
    request_url = models.CharField(max_length=250, blank=True,null=True)
    resp_code = models.CharField(max_length=250, blank=True,null=True)

class Registration(AbstractUser):
    # photoimage = models.FileField(blank=True, null=True)
    #user_id = models.CharField(max_length=100, unique=True,)
    employee_id = models.CharField(max_length=250, blank=False)
    skills = models.CharField(max_length=250, blank=False)
    hobbies = models.CharField(max_length=250, blank=False)
    account_no = models.IntegerField()
    ifsc_code = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    password = models.CharField(max_length=250, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    SEX = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    )
    gender = models.CharField(choices=SEX, max_length=10)
    #email = models.EmailField(max_length=250)
    father_name = models.CharField(max_length=100)
    #joining_date = models.DateField(blank=True)
    dob = models.DateField(blank=True)
    spouse_name = models.CharField(max_length=100)
    current_residency_address = models.CharField(max_length=100)
    current_zip_code = models.CharField(max_length=20)
    current_state = models.CharField(max_length=100)
    current_country = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    permanent_zip_code = models.CharField(max_length=20)
    permanent_state = models.CharField(max_length=100)
    permanent_country = models.CharField(max_length=100)
    personal_contact_no = models.IntegerField(blank=True)
    emergency_contact_no = models.IntegerField(blank=True)
    highest_education = models.CharField(max_length=250, blank=True)
    educational_institute_name = models.CharField(max_length=250, blank=True)
    year_of_passing = models.DateField(blank=True)
    previous_employee_name = models.CharField(max_length=250, blank=True)
    previous_empoyee_from = models.DateField(blank=True)
    previous_empoyee_to = models.DateField(blank=True)
    # photoidproofimage = models.FileField(blank=True, null=True)
    pan_no = models.CharField(max_length=250, blank=True)
    bank_name_for_salary = models.CharField(max_length=100)
    #active_user = models.BooleanField()
    is_active = models.BooleanField()

    Empinfo = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Other', 'Other'),
    )
    employee_info = models.CharField(choices=Empinfo, max_length=10)
    agreeterms = models.BooleanField()
    profilepic = models.ImageField(upload_to='images/')
    experience_documents =models.ImageField(upload_to='images/')


    def __str__(self):
        return self.username


class UserImagesUpload(models.Model):
    name = models.CharField(max_length=50)
    userprofile = models.ImageField(upload_to='images/')

class OptionalSchemeURLValidator(URLValidator):
    def __call__(self, value):
        if '://' not in value:
            # Validate as if it were http://
            value = 'http://' + value
        super(OptionalSchemeURLValidator, self).__call__(value)

class Addurl_project_Model(models.Model):
    Tenantid = models.CharField(max_length=250,blank=False,unique=True)
    tenant_url =models.CharField(max_length=250,unique=True)



    def __str__(self):
        return (self.Tenantid,self.tenant_url)


