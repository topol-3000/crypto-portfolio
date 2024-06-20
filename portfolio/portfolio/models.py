from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
