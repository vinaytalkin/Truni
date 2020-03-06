from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render


def sendemail(request,subject='',bodymessage='',senderfrom='',senderto=''):
    mess = ''
    subject = "Hello  "
    bodymessage = 'Automated Message send from system dont reply back'
    senderfrom = 'kvkvinay224@gmail.com'
    senderto = ['',]
    send_mail(subject,bodymessage,senderfrom,[senderto],
              fail_silently=False)
    return render(request,'email.html',{'message':mess})
