from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from authentication.forms import AuthForm
from authentication.forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        f'{reverse("home")}?status_massage=Вы успешно вошли в систему!'
                    )
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя неактивна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form,
        'title': 'Login page',
    }
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return render(request, 'logout.html', {'title': 'Exit'})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            city = form.cleaned_data.get('city')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

