from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def galery(request):
    return render(request, 'main/galery.html')

def politic(request):
    return render(request, 'main/politic.html')

def product(request):
    return render(request, 'main/product.html')

def contact(request):
    return render(request, 'main/contact.html')

def beton(request):
    return render(request, 'main/beton.html')

def smtp(request):
        if request.method == "POST":
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']
            message = request.POST ['message']

            # send an email
            send_mail(
                message_name,
                message,
                message_email,
                ['']
            )
        return render(request, 'main/smtp.html')
    
def parners(request):
    return render(request, 'main/parners.html')
