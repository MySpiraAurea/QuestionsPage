from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import LoginForm


def user_login(request):
    template = 'login/login.html'
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('questions:questions')
            else:
                error_message = "Неверное имя пользователя или пароль."
    else:
        form = LoginForm()
    return render(request, template, {'form': form, 'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('homepage:index')
