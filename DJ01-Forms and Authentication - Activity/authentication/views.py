from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm
from .models import Profile

# Create your views here.


def home_view(request: HttpRequest):
    if request.user.is_authenticated:
        return render(request, "home.html")

    else:
        return HttpResponseRedirect("/login/")


def logout_view(request: HttpRequest):
    logout(request)

    return HttpResponseRedirect("/login/")


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                request, username=data["username"], password=data["password"]
            )

            print(user)

            if user is not None:
                login(request, user)

                return HttpResponseRedirect("/home/")

    return render(request, "login.html", {"form": LoginForm()})


def register_view(request: HttpRequest):
    if request.method == "POST":
        # register new user

        form = RegistrationForm(request.POST)

        is_valid = form.is_valid()
        data = form.cleaned_data

        if is_valid and data["password1"] == data["password2"]:
            user = User(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["username"],
                email=data["email"],
                password=data["password2"],
            )

            profile = Profile(user=user)

            user.set_password(data["password2"])
            user.save()
            profile.save()

            return HttpResponseRedirect("/home/")

        else:
            # send a form
            form = RegistrationForm()

            return render(request, "register.html", {"form": form})

    else:
        # send a form
        form = RegistrationForm()

        return render(request, "register.html", {"form": form})
