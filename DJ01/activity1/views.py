from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

# Create your views here.


def profile_view(request: HttpRequest):
    params = request.GET

    first_name = params.get("first_name")

    user = User.objects.get(first_name=first_name)
    profile = Profile.objects.get(user=user)

    print(profile.profile_picture)

    return render(
        request,
        "profile.html",
        {
            "first_name": profile.user.first_name,
            "last_name": profile.user.last_name,
            "profile_picture": profile.profile_picture,
        },
    )


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        print("FORM BE LIKE", form.is_valid())

        if form.is_valid():
            user = form.save()

            profile = Profile(user=user)

            profile.save()

            return HttpResponseRedirect("/activity1/home")

        print(form.errors)

    else:
        form = UserCreationForm()

        return render(request, "register.html", {"form": form})


def home_view(request):
    return render(request, "home.html")
