from django.contrib import sessions
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View

from carts.mixins import CartMixin
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            # Если нет, то создаем новую корзину с этим продуктом
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=(
                    request.session_key if not request.user.is_authenticated else None
                ),
                product=product,
                quantity=1,
            )

        response_data = {"message":"Товар добавлен в корзину!",
                                        "cart_items_html": self.render_cart(request)}

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.get("quantity")
        cart.save()

        quantity = cart.quantity

        response_data = {
            "message":"Количество изменено!",
            "cart_items_html": self.render_cart(request),
            "quantity": quantity,
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = self.get_cart(request, cart_id=cart_id)
        quantity = cart.quantity

        cart.delete()

        response_data = {
            "message":"Товар удален из корзины!",
            "cart_items_html": self.render_cart(request),
            "quantity_deleted": quantity,
        }

        return JsonResponse(response_data)


# Create your views here.
# def cart_add(request):
#     #Достаю объект продукта по id из ajax запроса
#     product_id = request.POST.get("product_id")
#     product = Products.objects.get(id=product_id)

#     #Если пользователь зареган, то достаем все его корзины с этим продуктом
#     if request.user.is_authenticated:
#         carts=Cart.objects.filter(user=request.user,product=product)

#         #Если корзины есть, то берем первую, и добавляем количество +1, сохраняем
#         if carts.exists():
#             cart =carts.first()
#             if cart:
#                 cart.quantity+=1
#                 cart.save()
#         else:
#             #Если нет, то создаем новую корзину с этим продуктом
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         carts=Cart.objects.filter(session_key=request.session.session_key,product=product)

#         #Если корзины есть, то берем первую, и добавляем количество +1, сохраняем
#         if carts.exists():
#             cart =carts.first()
#             if cart:
#                 cart.quantity+=1
#                 cart.save()
#         else:
#             #Если нет, то создаем новую корзину с этим продуктом
#             Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

#     user_cart = get_user_carts(request)

#     cart_items_html =render_to_string(
#         'carts/includes/included_cart.html',
#         {"carts":user_cart},
#         request=request
#     )

#     response_data={
#         'message':'Товар добавлен в корзину',
#         'cart_items_html':cart_items_html,
#     }
#     #редирект на ссылающую страницу
#     return JsonResponse(response_data)

# def cart_change(request):
#     cart_id = request.POST.get('cart_id')
#     quantity=request.POST.get('quantity')

#     cart = Cart.objects.get(id=cart_id)
#     cart.quantity=quantity
#     cart.save()
#     upd_qua = cart.quantity

#     user_cart = get_user_carts(request)

#     cart_items_html =render_to_string(
#         'carts/includes/included_cart.html',
#         {"carts":user_cart},
#         request=request
#     )

#     response_data={
#         'message':'Количество изменено',
#         'cart_items_html':cart_items_html,
#         'quantity':upd_qua,
#     }


#     return JsonResponse(response_data)

# def cart_remove(request):
#     cart_id = request.POST.get('cart_id')
#     cart = Cart.objects.get(id=cart_id)
#     quantity=cart.quantity
#     cart.delete()

#     user_cart = get_user_carts(request)

#     cart_items_html =render_to_string(
#         'carts/includes/included_cart.html',
#         {"carts":user_cart},
#         request=request
#     )

#     response_data={
#         'message':'Товар удален',
#         'cart_items_html':cart_items_html,
#         'quantity_deleted':quantity,
#     }


#     return JsonResponse(response_data)
