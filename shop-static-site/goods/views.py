from itertools import product
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from goods.models import Categories, Products
from goods.utils import q_search


class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "products"
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get("on_sale", None)
        order_by = self.request.GET.get("order_by", None)
        query = self.request.GET.get("q", None)

        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)
        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slug"] = self.kwargs.get("category_slug")
        return context


# Create your views here.
# from goods.models import Products
# from goods.utils import q_search

# def catalog(request, category_slug=None):

#     page = request.GET.get('page',1)
#     on_sale = request.GET.get('on_sale',None)
#     order_by = request.GET.get('order_by',None)
#     query=request.GET.get('q',None)

#     if category_slug == 'all':
#         goods = Products.objects.all()
#     elif query:
#         goods=q_search(query)
#     else:
#         goods = Products.objects.filter(category__slug=category_slug)

#     if on_sale:
#         goods=goods.filter(discount__gt=0)

#     if order_by and order_by!="default":
#         goods=goods.order_by(order_by)

#     paginator = Paginator(goods, 8)
#     current_page = paginator.page(int(page))
#     slug_url = category_slug

#     context ={
#         'products':current_page,
#         'slug':slug_url
#     }
#     return render(request, 'goods/catalog.html',context=context)


class ProductView(DetailView):
    # model = Products
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=...):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product


# def product(request, product_slug):
#     product = Products.objects.get(slug=product_slug)

#     context ={
#         'product':product
#     }
#     return render(request, 'goods/product.html',context=context)
