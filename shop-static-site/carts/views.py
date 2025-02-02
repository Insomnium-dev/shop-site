
from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products

# Create your views here.
def cart_add(request):
    #Достаю объект продукта по id из ajax запроса
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    #Если пользователь зареган, то достаем все его корзины с этим продуктом
    if request.user.is_authenticated:
        carts=Cart.objects.filter(user=request.user,product=product)

        #Если корзины есть, то берем первую, и добавляем количество +1, сохраняем
        if carts.exists():
            cart =carts.first()
            if cart:
                cart.quantity+=1
                cart.save()
        else:
            #Если нет, то создаем новую корзину с этим продуктом
            Cart.objects.create(user=request.user, product=product, quantity=1)
        

    
    user_cart = get_user_carts(request)
    
    cart_items_html =render_to_string(
        'carts/includes/included_cart.html',
        {"carts":user_cart},
        request=request
    )

    response_data={
        'message':'Товар добавлен в корзину',
        'cart_items_html':cart_items_html,
    }
    #редирект на ссылающую страницу
    return JsonResponse(response_data)

def cart_change(request, product_slug):
    pass

def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    return redirect(request.META['HTTP_REFERER'])