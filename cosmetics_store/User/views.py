from django.shortcuts import render, redirect, get_object_or_404
from .forms import Login, Register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def login_account(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid password or login')
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
            if User.objects.filter(username=cd['username']):
                messages.error(request, 'Имя занято')
            else:  
                user = User.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'])
                Profile.objects.create(user=user, phone = cd['phone'], age=cd['age'])
                login(request, user)
                return redirect('home')
    else:
        form = Register()
    return render(request, 'register.html', {'form':form})


def profile_vies(request):
    profile = get_object_or_404(Profile, user = request.user)
    return render(request, 'profile.html', {'profile':profile})