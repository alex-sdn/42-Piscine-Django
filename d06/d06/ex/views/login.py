from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ex.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Incorrect username or password')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'page': 'login',
        'username': request.session.get('username')
    }
    return render(request, 'ex/login_signup.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            #create Profile for permissions
            Profile.objects.create(user=user)

            login(request, user)

            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'page': 'signup',
        'username': request.session.get('username')
    }
    return render(request, 'ex/login_signup.html', context)