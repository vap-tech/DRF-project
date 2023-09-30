from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    patronymic = models.CharField(max_length=35, verbose_name='отчество', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    verification_code = models.IntegerField(verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
