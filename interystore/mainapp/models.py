from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя категории',
        max_length=45,
        unique=True
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True

    )

    def __str__(self):
        return f'ProductCategory: {self.name} {self.pk}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'




class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128
    )
    image = models.ImageField(
        upload_to='product_images',
        blank=True
    )
    short_desc = models.TextField(
        verbose_name='краткое описание продукта',
        max_length=60,
        blank=True
    )
    description = models.TextField(
        verbose_name='описание продукта',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )


    def __str__(self):
        return f'Product: {self.name} {self.pk}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'