from ctypes import cast
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import context
from django.template.base import constant_string
from django.template.defaultfilters import truncatechars

# Create your views here.
from goods.models import Products
from goods.utils import q_search

def catalog(request, category_slug=None):

    page = request.GET.get('page',1)
    on_sale = request.GET.get('on_sale',None)
    order_by = request.GET.get('order_by',None)
    query=request.GET.get('q',None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods=q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods=goods.filter(discount__gt=0)

    if order_by and order_by!="default":
        goods=goods.order_by(order_by)
    
    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))
    slug_url = category_slug

    context ={
        'products':current_page,
        'slug':slug_url
    }
    return render(request, 'goods/catalog.html',context=context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context ={
        'product':product
    }
    return render(request, 'goods/product.html',context=context)