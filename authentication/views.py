from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib import auth


def home(request):
    return render(request, 'home.html')

def loginform(request):
    if request.user.is_authenticated:
    
        return redirect("home")

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
       
    
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
       
    return render(request, 'login.html', {"status":False})



def signupview(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = CustomUser.objects.create_user(username=email, email=email, password=password,  last_name=last_name, first_name=first_name, is_admin=False)
        login(request, user)

        #request.session['account_created'] = True
        return redirect('/')
    return render(request, 'signup.html')


def logoutview(request):
    logout(request)
    return redirect("login")