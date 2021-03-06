from django.shortcuts import render, HttpResponseRedirect
from accounts.forms import LoginForm, RegisterForm, EditForm
from images.models import Image
from django.contrib import auth
from django.urls import reverse

# Create your views here.

def login_view(request):
    title = 'вход'
    form = LoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {'title': title, 'login_form': form}
    return render(request, 'accounts/login.html', content)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        register_form = RegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'accounts/register.html', content)

def edit_view(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = EditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid(): # error for avatar
            edit_form.save()
            return HttpResponseRedirect(reverse('accounts:edit'))
    else:
        edit_form = EditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'accounts/edit.html', content)