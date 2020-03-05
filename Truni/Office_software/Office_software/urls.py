"""servicecenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path,include
from center.views import home_view, career_view,editandsubmit,view_projectUrls,testing_view, logout_view, contactus_view,Registration_view, Login_view, aboutus_view,userdetails_view,Forgotpassword_view,previewdetails
from center.form import Registration_model,Registration_Preview
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('admin/', admin.site.urls),
    path('',home_view),
    path('home/',home_view),
    path('career/',career_view),
    #path('contactus/',contactus_view,name='contactus'),
    path('register/',Registration_view),
    path('signin/',Login_view,name='login'),
    path('aboutus/',aboutus_view),
    path('userprofile/',userdetails_view,name='userprofile'),
    path('forgot_password/',Forgotpassword_view),
    path('preview/',previewdetails,name='preview'),
    path('editandsubmit/',editandsubmit,name='editandsubmit'),
    #path('contactus/',myview,name='contactus'),
    path('logout/',logout_view,name='logout'),
    path('testing/',testing_view,name='testing'),
    path('projecturl/',view_projectUrls,name='projecturl'),
    #re_path('grid_json/', djqgrid.urls),


    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)