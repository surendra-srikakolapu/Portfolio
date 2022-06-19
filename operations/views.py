from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import *
from django.core.mail import send_mail


# Create your views here.

def index(request):

    files = Upload_download_file.objects.all()

    if request.method == "POST":

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = {
            'fullname':fullname,
            'email':email,
            "message":message
        }

        message = '''
        New message:{}

        From:{}
        '''.format(context['message'],context['email'])

        

        send_mail(context['fullname'] , message , '' ,['surendra.srikakolapu1@gmail.com'])

        messages.success(request, 'Message sent successfully !')


        
    else:
        files = Upload_download_file.objects.all()    
    return render(request, 'index.html', {'files': files})



def Files(request):

    files = Upload_download_file.objects.all()

    return render(request, 'download_list.html', {'files': files})
