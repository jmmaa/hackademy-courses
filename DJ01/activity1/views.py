from django.http import HttpRequest
from django.shortcuts import render


from django.contrib.auth.models import User

from .models import Profile

# Create your views here.


def profile(request: HttpRequest):
    params = request.GET

    first_name = params.get("first_name")

    user = User.objects.get(first_name=first_name)
    profile = Profile.objects.get(user=user)

    print(profile.profile_picture)

    return render(
        request,
        "index.html",
        {
            "first_name": profile.user.first_name,
            "last_name": profile.user.last_name,
            "image": profile.profile_picture,
        },
    )
