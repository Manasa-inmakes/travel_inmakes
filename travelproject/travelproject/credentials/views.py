from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            print("login")
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return  redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method== 'POST':
        uname = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        if pwd == pwd1:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already Taken")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already Taken")
                return  redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=firstname, last_name=lastname, email=email,password=pwd)
                user.save();
                return  redirect('login')
            print("User Created")
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return  redirect('/')
    return  render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
