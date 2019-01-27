from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


def get_now():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
    )

    age = models.SmallIntegerField(
        verbose_name='возраст'
    )

    activation_key = models.CharField(
        max_length=128,
        blank=True
    )

    activation_key_expire = models.DateTimeField(
        default=get_now
    )

    def is_activation_key_expared(self):
        if now() <= self.activation_key_expire:
            return False
        else:
            return True