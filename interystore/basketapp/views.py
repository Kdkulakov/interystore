from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket
from mainapp.views import get_basket
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse




@login_required
def index(request):
    context = {
        'basket': get_basket(request.user)
    }
    return render(request, 'basketapp/basket.html', context)

@login_required
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
        print(f'Добавлен продукт {product} в корзину')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
