from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_pic_url = models.URLField(null=True, blank=True)