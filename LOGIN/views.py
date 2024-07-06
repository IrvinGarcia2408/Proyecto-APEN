from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "principal/base.html", {"user":request.user})  

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(inicio)
        else:
            messages.info(request, 'Nombre de usuario o contraseña incorrectos')
            return redirect(login)
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['first_last_name']+ " " + request.POST['second_last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'El usuario que ingreso ya existe')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'El usuario ha sido creado correctamente')
                return redirect(login)
        else:
            messages.info(request, 'Las contraseña no coincide con la confirmación')
            return redirect(register)
    else:
        return render(request, 'register.html')

def logout_user(request):
    auth.logout(request)
    return redirect(index)
