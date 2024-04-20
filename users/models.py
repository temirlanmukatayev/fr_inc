
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_client = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


class Worker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                primary_key=True)
    experience = models.IntegerField('опыт', blank=True, null=True)
    sphere = models.CharField('сфера', blank=True, max_length=100)
    description = models.TextField('описание', blank=True)
