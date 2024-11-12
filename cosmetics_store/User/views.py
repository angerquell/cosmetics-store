from django.shortcuts import render, redirect
from .forms import Login, Register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def login_account(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user)
            return redirect('home')
    else: 
        form = Login()
    return render(request, 'login.html', {'form':form})


def logout_account(request):
    logout(request)
    return redirect('home')


def register_account(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'])
            login(request, user)
            return redirect('home')
    else:
        form = Register()
    return render(request, 'register.html', {'form':form})