import re
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30, unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Username must contain only letters, digits or the '
                'following characters: @/./+/-/_', 'invalid'
            )
        ]
    )

    email = models.EmailField(verbose_name='e-mail', unique=True)
    name = models.CharField(verbose_name='name', max_length=100, blank=True)

    is_active = models.BooleanField(
        verbose_name='is active?', blank=True, default=True)
    is_staff = models.BooleanField(
        verbose_name='is staff?', blank=True, default=False)
    date_joined = models.DateTimeField(
        verbose_name='joined in',
        auto_now_add=True, editable=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
