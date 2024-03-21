from django.db import models

from django.contrib.auth.models import User

# Create your models here.


# activity 2


class Profile(models.Model):
    profile_picture = models.ImageField(blank=True)
    description = models.CharField(max_length=250)

    # activity 3

    # name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
