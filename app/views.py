from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def form(request):
    if request.method == "POST":
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Test',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
    return render(request,'form.html')