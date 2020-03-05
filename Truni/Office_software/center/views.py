from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_tables2 import SingleTableView
from formtools.preview import FormPreview
from formtools.wizard.views import SessionWizardView
#from django.contrib.auth.hashers import make_password
from center.form import Registration_model,Addurl_project_Model, Registration_Preview, MyGrid, Addurl_project_form  # RegistrationForm
from center.models import Registration
from django.contrib.auth.decorators import login_required
# Create your views here.

import pdb;


def Registration_view(request):
    mess = ''
    if request.method == 'POST':
        data = request.POST
        form = Registration_model(request.POST,request.FILES)
        password = data.get("password")
        password_confirm = data.get("password_confirm")
        if password == password_confirm:
            data = request.POST
            if form.is_valid():
                try:
                    user = form.save()
                    user.set_password(data.get("password"))
                    user.save()
                    mess = "User Profile Created Success..!!"
                    print(mess)
                    form.full_clean()
                except Exception as ex:
                    mess = ex
            else:
                print(form.errors)
                mess = form.errors
        else:
            mess = "password and Conform passswprd not same"
            print(mess)
    else:
        form = Registration_model()
    return render(request, 'center/RegistrationForm.html', {'form': form, 'message': mess})  # RegistrationForm


def Login_view(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        #user = Registration.objects.filter(username=username, password=password)
        user = authenticate(username=username,password=password)
        import pdb
        #pdb.set_trace()
        try:
            if user is not None:
                #pdb.set_trace()
                login(request,user)
                msg = "authenticated"
                next_url = request.GET.get("next", "userpage/")
                return redirect(userdetails_view)
            else:
                msg = "Not Authenticated..!!"
        except:
            msg = "not authenticated"

    return render(request, "center/signin.html", {"message": msg})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect(Login_view)
#@login_required(login_url='/signin/')
def userdetails_view(request):
    msg = ""
    #import pdb;pdb.set_trace()
    user = request.user
    #import pdb;pdb.set_trace()
    pass
    return render(request, "center/userprofile.html", {"message": msg,'user':user})

def testing_view(request):
    urldata=''
    mess = ''
    #data = Addurl_project_Model.objects.all()
    if request.method =='POST':
        form = Addurl_project_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =Addurl_project_form()
    return render(request, 'center/projecturls.html', {'form': form, 'message': mess})

def view_projectUrls(request):
    data =''
    if request.method =='POST':
        data = Addurl_project_Model.objects.all()
    else:
        data = Addurl_project_Model.objects.all()
    return render(request, 'center/viewprojecturls.html', {'data':data})


def edit_userprofile(request):
    pass

def previewdetails(request):
    if request.method == 'GET':
        form = Registration_model()
        #form = Registration_model(instance=form)
        for fieldname in form.fields:
            form.fields[fieldname].disabled = True
        return render(request, 'center/preview.html', {'form': form})

def editandsubmit(request):
    mess = ''
    if request.method == 'GET':
        data = request.POST
        newset= data[0]
        form = Registration_model(instance=newset)

    else:
        form = Registration_model()
        # form_choice = ChoiceFieldForm()
    return render(request, 'center/RegistrationForm.html', {'form': form, 'message': mess})

def myview(tables):
    grid = MyGrid()
    table_class = MyGrid()
    grid = Registration.objects.all()
    template_name = "center/contactus.html"
    #return render('center/contactus.html', { grid: grid })



def Forgotpassword_view(request):
    return render(request, "center/forgotpassword.html")




def home_view(request):
    return render(request, 'center/home.html')


def career_view(request):
    return render(request, 'center/career.html')



def contactus_view(request):


    return render(request, 'center/contactus.html')#{'form': form}


def aboutus_view(request):
    return render(request, 'center/aboutus.html')

