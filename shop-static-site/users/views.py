from email import message
from operator import rshift
from django.core.signals import request_started
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, вы успешно авторизованы!')
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "users/registration.html", context)

@login_required
def profile(request):

    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Сохранено!')
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {"form": form}
    return render(request, "users/profile.html", context)

@login_required
def logout(request):
    auth.logout(request)
    messages.warning(request, 'Вы вышли из профиля!')
    return redirect(reverse("main:index"))
