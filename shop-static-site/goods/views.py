from django.shortcuts import render
from django.template import context

# Create your views here.
from goods.models import Products

def catalog(request):
    return render(request, 'goods/catalog.html')


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context ={
        'product':product
    }
    return render(request, 'goods/product.html',context=context)