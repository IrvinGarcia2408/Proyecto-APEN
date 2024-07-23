from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


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

@login_required
def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['first_last_name']+ " " + request.POST['second_last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email

            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)  # Important to keep the user logged in after password change              
            
            user.save()
            return redirect(inicio)
        else:
            messages.info(request, 'La contraseña no coincide con la confirmación')
            return redirect('profile')
    else:
        print("si entramos")
        user = request.user
        first_last_name, second_last_name = user.last_name.split(' ', 1) if ' ' in user.last_name else (user.last_name, '')
        context = {
            'user': user,
            'first_last_name': first_last_name,
            'second_last_name': second_last_name,
        }

        return render(request, 'edit_profile.html', context)

def logout_user(request):
    auth.logout(request)
    return redirect(index)

