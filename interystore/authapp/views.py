from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def user_login(request):

    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print("Форма заполнена корректно")
            if user:
                login(request, user)
                # return HttpResponseRedirect('/')
                return HttpResponseRedirect(reverse('main:main'))

    else:
        form = ShopUserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('main:main'))

def user_register(request):

    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('main:main'))

    else:
        form = ShopUserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def user_update(request):

    if request.method == 'POST':
        form = ShopUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('main:main'))

    else:
        form = ShopUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'authapp/register.html', context)