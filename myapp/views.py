from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import models
from myapp.models import Register
# import mysql.container
# Create your views here.
def Index(request):
    if request.method == 'POST':
        email = request.POST('email')
        password = request.POST('password')

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('register')
        else:
            messages.info(request,'invalid detalils')
            return redirect('index')
    else:
        return render(request, 'myapp/index.html')
def register(request):
    return render(request, 'myapp/register.html')
def login(request):
    if request.method == 'POST':
        email = request.POST('email')
        password = request.POST('password')

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('done')
        else:
            messages.info(request,'invalid detalils')
            return redirect('login')
    else:
        return render(request, 'myapp/login.html')
def succ(request):
    if request.method == 'POST':
        regobj = models.Register()
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password==confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                regobj.username = username
                regobj.email = email
                regobj.phone = phone
                regobj.password = password
                regobj.confirmpassword = confirmpassword
                user = User.objects.create_user(username=username, email=email, password=password)
                regobj.save()
        else:
            messages.info(request,'enter the same password')
            return redirect('register')
        return redirect('succ')
    else:
         return render(request, 'myapp/succ.html')

def done(request):

        return render(request, 'myapp/done.html')