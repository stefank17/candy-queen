from django.contrib.auth.models import User
from django.db import models
from candy.models import Candy


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)