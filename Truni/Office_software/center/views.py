from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.views import auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django_tables2 import SingleTableView
from formtools.preview import FormPreview
#from formtools.wizard.views import SessionWizardView
# from django.contrib.auth.hashers import make_password
from center.form import Registration_model, Addurl_project_Model, Registration_Preview, \
    Addurl_project_form  # RegistrationForm
from center.models import Registration
from django.contrib.auth.decorators import login_required
# Create your views here.

import pdb;


def Registration_view(request):
    mess = ''
    if request.method == 'POST':
        data = request.POST
        form = Registration_model(request.POST, request.FILES)
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
        # user = Registration.objects.filter(username=username, password=password)
        user = authenticate(username=username, password=password)
        import pdb
        # pdb.set_trace()
        try:
            if user is not None:
                # pdb.set_trace()
                login(request, user)
                msg = "authenticated"
                next_url = request.GET.get("next", "userpage/")
                return redirect(userdetails_view)
            else:
                msg = "Not Authenticated..!!"
        except:
            msg = "not authenticated"

    return render(request, "center/signin.html", {"message": msg})

@login_required(login_url='/signin/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect(Login_view)


# @login_required(login_url='/signin/')
@login_required(login_url="/signin/")
def userdetails_view(request):
    msg = ""
    # import pdb;pdb.set_trace()
    user = request.user
    formdata = Registration.objects.get(pk=user.id)
    # import pdb;pdb.set_trace()
    pass
    return render(request, "center/userprofile.html", {"message": msg, 'user': user, 'formdata':formdata})


@login_required(login_url="/signin/")
def testing_view(request):
    urldata = ''
    mess = ''
    # data = Addurl_project_Model.objects.all()
    if request.method == 'POST':
        form = Addurl_project_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Addurl_project_form()
    return render(request, 'center/projecturls.html', {'form': form, 'message': mess})

@login_required(login_url='/signin/')
def view_projectUrls(request):
    data = ''
    if request.method == 'POST':
        data = Addurl_project_Model.objects.all()
    else:
        data = Addurl_project_Model.objects.all()
    return render(request, 'center/viewprojecturls.html', {'data': data})


def edit_userprofile(request):
    pass


def previewdetails(request):
    if request.method == 'GET':
        form = Registration_model()
        # form = Registration_model(instance=form)
        for fieldname in form.fields:
            form.fields[fieldname].disabled = True
        return render(request, 'center/preview.html', {'form': form})


def editandsubmit(request):
    mess = ''
    if request.method == 'GET':
        data = request.POST
        newset = data[0]
        form = Registration_model(instance=newset)

    else:
        form = Registration_model()
        # form_choice = ChoiceFieldForm()
    return render(request, 'center/RegistrationForm.html', {'form': form, 'message': mess})


# def myview(tables):
#     grid = MyGrid()
#     table_class = MyGrid()
#     grid = Registration.objects.all()
#     template_name = "center/contactus.html"
#     # return render('center/contactus.html', { grid: grid })


def Forgotpassword_view(request):
    return render(request, "center/forgotpassword.html")


def home_view(request):
    return render(request, 'center/home.html')


def career_view(request):
    return render(request, 'center/career.html')


def contactus_view(request):
    return render(request, 'center/contactus.html')  # {'form': form}


def aboutus_view(request):
    return render(request, 'center/aboutus.html')

#-------------------Pdf------------------
from django.http import HttpResponse
from django.views.generic import View

from center.pdfcreation import render_to_pdf #created in step 4
import datetime


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
