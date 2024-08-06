from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from portfolio.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return f"User(full_name={self.full_name}; email={self.email})"


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10, unique=True)
    image = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.name}({self.ticker}): Price: ${self.price}, Market Cap: ${self.market_cap}."
