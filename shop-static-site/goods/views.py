from ctypes import cast
from django.shortcuts import render
from django.template import context
from django.template.base import constant_string
from django.template.defaultfilters import truncatechars

# Create your views here.
from goods.models import Products

def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    

    context ={
        'products':goods
    }
    return render(request, 'goods/catalog.html',context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context ={
        'product':product
    }
    return render(request, 'goods/product.html',context=context)