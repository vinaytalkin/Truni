from django.http import HttpResponse
from django.shortcuts import render, redirect
from center.models import Registration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import pdb

def home_view(request):
    return render(request, 'center/home.html')


def career_view(request):
    return render(request, 'center/career.html')


def register_view(request):
    msg = ""
    if request.method.lower() == "post":
        data = request.POST
        user = Registration(first_name=data.get("fname"),
                            last_name=data.get("Lstname"),
                            username=data.get("Usd"),
                            password=data.get("password"),
                            confirmpassword=data.get("cnfpassword"),
                            email=data.get("email"),
                            address=data.get("address"),
                            phone=data.get("phone"),
                            Image=data.get("img"),
                            fathername=data.get("img"),
                            dob=data.get("img"),
                            spouse_name=data.get("img"),
                            married_anv=data.get("img"),
                            current_add=data.get("img"),
                            personal_contactno=data.get("img"),
                            emergencyno=data.get("img"),
                            highest_education=data.get("img"),
                            education_instituename=data.get("img"),
                            year_passing=data.get("img"),
                            firstemployee_name=data.get("img"),
                            employee_from=data.get("img"),
                            employee_to=data.get("img"),
                            photo_id=data.get("img"),
                            pan_no=data.get("img"),
                            bank_accountno=data.get("img"),
                            bank_branch=data.get("img"),
                            bank_ifsccode=data.get("img"),
                            Jdate=data.get("img"),
                            sex=data.get("img"))
        try:
            user.save()
            user.set_password(data.get("password"))
            user.set_password(data.get("cnfpassword"))
            user.save()
            messages.INFO("user created successfully")
            return redirect('/')
        except Exception as err:
            msg = str(err)

    else:
        print("password not matching")
    return render(request, 'center/register.html', {"message": msg})


def contactus_view(request):
    return render(request, 'center/contactus.html')


def signin_view(request):
    msg = ''

    if request.method.lower() == 'POST':
        pdb.set_trace()
        username = request.post['uname']
        password = request.post['psw']


        user = authenticate(request, username=username, password=password)
        msg = "username and password are " + username, password

        # if user is not None:
        # 	auth.login(request,user)
        # 	print("login success")
        if user:
            login(request, user)
            msg = "authenticated"
        else:
            msg = "print unable to logins"
            return redirect('/')

    return render(request, 'center/signin.html', {"message": msg})


def aboutus_view(request):
    return render(request, 'center/aboutus.html')
