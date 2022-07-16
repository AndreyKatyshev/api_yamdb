from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'

ROLE_CHOICES = [
    ('user', 'User'),
    ('moderator', 'Moderator'),
    ('admin', 'Admin')
]


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='Почта'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
        blank=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )

    confirmation_code = models.CharField(
        max_length=70,
        unique=True,
        blank=True,
        null=True
    )

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def __str__(self):
        return self.username
