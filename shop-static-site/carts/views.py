
from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

# Create your views here.
def cart_add(request, product_slug):
    #Достаю объект продукта по слагу
    product = Products.objects.get(slug=product_slug)

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
            Cart.objects.create(user=request.user, product=product, quantity=1)\
            
    #редирект на ссылающую страницу
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    pass

def cart_remove(request, product_slug):
    pass
