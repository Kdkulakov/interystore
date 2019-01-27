from django.contrib import admin
from authapp.models import ShopUser


@admin.register(ShopUser)
class AdminShopUser(admin.ModelAdmin):
    # fields = ('username', 'email', 'is_active')
    list_display = ('username', 'email', 'is_active')

