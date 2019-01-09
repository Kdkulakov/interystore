from django.urls import re_path
import basketapp.views as basketapp


app_name = 'basket'

urlpatterns = [
    re_path(r'^$', basketapp.index, name='index'),
    re_path(r'^add/(?P<product_pk>\d+)/$', basketapp.basket_add, name='add'),
]
