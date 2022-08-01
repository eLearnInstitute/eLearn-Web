from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if  request.user.is_anonymous:
        return redirect("/account/signin")
    

def account(request):
    return HttpResponse( "forget account page will display here")
    
def signup(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username already taken")
            elif User.objects.filter(email=email).exists():
                print("email id taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name,)
                user.save();
                return redirect('/account/signin')
    else:
       return render(request, "register.html") 
    return render(request, "register.html")
    
def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "logged in successfully")
            return redirect("/dashboard")
        else:
            messages.error(request, 'invalid creadentials')
            return redirect('/account/signin')
    else:
        return render(request, 'login.html')
    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")

    return redirect("/account/signin")
        

