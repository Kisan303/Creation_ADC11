from django.shortcuts import render, redirect
from .models import Register
from .forms import RegistrationForm
from .loginforms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(request):
	form = RegistrationForm()
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('account:home')
	return render(request,'registration/register.html', {"p":form})

def home(request):
	return render(request, 'registration/home.html')


def login(request):
    form = LoginForm()
    if request.method == "POST":
       username = request.POST['user']
       password = request.POST['password']
       
       user = authenticate(username=username,password=password)
       #login(request, user)
       return redirect('account:home')
    return render(request,'registration/login.html', {"form":form})