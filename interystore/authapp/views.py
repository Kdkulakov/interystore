from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from .models import ShopUser

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
            user = form.save()
            if send_verify_email(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('main:main'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
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


def send_verify_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} \
                перейти по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.activation_key_expire:
            user.is_active = True
            user.save()
            login(request, user)
        else:
            print(f'error activation user: {user}')
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user: {e} -> {e.args}')
        return HttpResponseRedirect(reverse('main:main'))