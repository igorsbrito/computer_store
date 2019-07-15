from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=120, verbose_name='Full Name')
    email = models.CharField(max_length=120, verbose_name='Email', unique=True)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.email)