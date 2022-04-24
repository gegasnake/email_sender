from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.core.mail import send_mail


@csrf_protect
def index(request):
    return render(request, 'send_email/registration_form.html')


def registered(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        username = request.POST['username']

        user = User.objects.create_user(username=username, password=password, email=email,)
        user.save()
        send_mail("site_register", "so this is a message to let you know that you registered successfully!",
                  "gegatvara@gmail.com", [user.email], fail_silently=False)
        print('user created')
        return render(request, "send_email/registered.html")
    else:
        return render(request, "send_email/registered.html")
