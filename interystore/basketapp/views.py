from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket


def index(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.all()


    context = {
        'page_title': 'главная',
        'basket': basket,
    }
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, product_pk):
    # print(product_pk)
    # print(request.META.keys())

    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.all()

    product = get_object_or_404(Product, pk=product_pk)
    basket_item = Basket.objects.filter(product=product, user=request.user).first()
    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
        print(f'Продукт {product} обновлен')
    else:
        Basket.objects.create(product=product, user=request.user, quantity=1)
        print(f'Добавлен продукт {product} в крзину')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
