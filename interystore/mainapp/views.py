from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
import random

def get_basket(user):
    if user.is_authenticated:
        return user.basket_set.all().order_by('product__category')
    return []

def main(request):
    context = {
        'title': 'главная',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_pk=None):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    if category_pk:
        if category_pk != '0':
            products = Product.objects.filter(category__pk=category_pk)
        context = {
            'title': 'каталог',
            'products': products,
            'categories': categories,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', context)
    else:
        hot_product = random.choice(products)
        same_products = Product.objects.filter(category=hot_product.category). \
            exclude(pk=hot_product.pk)

        context = {
            'title': 'каталог',
            'categories': categories,
            'basket': get_basket(request.user),
            'hot_product': hot_product,
            'same_products': same_products,
        }
        return render(request, 'mainapp/products.html', context)


def product(request, pk):
    categories = ProductCategory.objects.all()

    context = {
        'title': 'продукты',
        'categories': categories,
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/products.html', context)


def detail(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.all()

    context = {
        'page_title': 'детали',
    }
    return render(request, 'mainapp/detail.html', context)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.all()

    locations = [
        {
            'city': 'COLIFORNIA',
            'phone': '1900-1234-5678',
            'email': 'info@interior.com',
            'address': '12 W 1st St. 90001 Los Angeles. Colifornia',
        },
        {
            'city': 'LONDON',
            'phone': '+49-324-424-4444',
            'email': 'info@interior.com',
            'address': '12 W 1st St. 90001 Los Angeles. Colifornia',
        },
        {
            'city': 'SINGAPUR',
            'phone': '1900-1234-5678',
            'email': 'info@interior.com',
            'address': '12 W 1st St. 90001 Los Angeles. Colifornia',
        }

    ]


    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contacts.html', context)