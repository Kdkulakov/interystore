from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product
import datetime


class Basket(models.Model):
    user = models.ForeignKey(
        ShopUser,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='продукт'
    )
    quantity = models.SmallIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        auto_now=True,
        verbose_name='время добавления',

    )