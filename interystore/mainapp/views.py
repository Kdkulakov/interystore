from django.shortcuts import render
from mainapp.models import ProductCategory, Product

def main(request):
    context = {
        'page_title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'каталог',
        'products': products,
        'categories': categories,
    }
    return render(request, 'mainapp/products.html', context)

def detail(request):
    context = {
        'page_title': 'детали',
    }
    return render(request, 'mainapp/detail.html', context)

def contacts(request):
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