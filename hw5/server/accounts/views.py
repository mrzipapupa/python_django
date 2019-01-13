from django.shortcuts import render, HttpResponseRedirect, redirect
from accounts.forms import LoginForm, RegisterForm, EditForm
from images.models import Image
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import DefaultLoginForm

# Create your views here.

def login_view(request):
    success_url = reverse_lazy('main:index')
    title = 'вход'
    form = DefaultLoginForm()
    if request.method == 'POST':
        form = DefaultLoginForm(data=request.POST)

        if form.is_valid(): # если поля содержат нужную по формату информацию
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect(success_url)
    content = {'title': title, 'form': form} # форма с ошибками в случае неуспеха
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