from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product


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

    def _get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(_get_product_cost)

    def _get_total_quantity(self):
        # _items = Basket.objects.filter(user=self.user)
        _items = self.user.basket_set.all()
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    total_quantity = property(_get_total_quantity)

    def _get_total_cost(self):
        # _items = Basket.objects.filter(user=self.user)
        _items = self.user.basket_set.all()
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    total_cost = property(_get_total_cost)
