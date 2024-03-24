from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User


from .forms import RegistrationForm
from .models import Profile
# Create your views here.


def home_view(request: HttpRequest):
    return render(request, "home.html")


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

            user.save()
            profile.save()

            return HttpResponseRedirect("/home/")

        else:
            # some error logic later
            pass

    else:
        # send a form
        form = RegistrationForm()

        return render(request, "register.html", {"form": form})
