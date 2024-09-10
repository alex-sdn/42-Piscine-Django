from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class SignupForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username', 'password1', 'password2']


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'user does not exist')
            
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'incorrect password')

    context = {
        'form': form,
        'page': 'login'
    }
    return render(request, 'ex/login_signup.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            return redirect('/')
        else:
            print('form not valid awoo')

    context = {
        'form': form,
        'page': 'signup'
    }
    return render(request, 'ex/login_signup.html', context)