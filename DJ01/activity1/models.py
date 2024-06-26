from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)
    description = models.CharField(max_length=250)
