from email import message
from gc import get_objects
from operator import rshift
from webbrowser import get
from django.core.signals import request_started
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, UpdateView

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        session_key = self.request.session.session_key

        user = form.get_user()

        if user:
            auth.login(self.request, user)

            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        redirect_page = self.request.POST.get("next", None)
        if redirect_page and redirect_page != reverse("users:logout"):
            return redirect_page
        return reverse_lazy("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] =
        return context


class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:profile")
    form_class = UserRegistrationForm

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class UserProfileView(UpdateView, LoginRequiredMixin):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset = ...):
        return self.request.user
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders']= Order.objects.filter(user=self.request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product").order_by("-id"),
        ))
        return context
    

class UserCartView(TemplateView):
    template_name="users/user-cart.html"


@login_required
def logout(request):

    auth.logout(request)
    # messages.warning(request, 'Вы вышли из профиля!')
    return redirect(reverse("main:index"))

# def users_cart(request):
#     return render(request, "users/user-cart.html")

# @login_required
# def profile(request):

#     if request.method == "POST":
#         form = ProfileForm(
#             data=request.POST, instance=request.user, files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             # messages.success(request,'Сохранено!')
#             return HttpResponseRedirect(reverse("users:profile"))
#     else:
#         form = ProfileForm(instance=request.user)

#     orders = Order.objects.filter(user=request.user).prefetch_related(
#         Prefetch(
#             "orderitem_set",
#             queryset=OrderItem.objects.select_related("product").order_by("-id"),
#         )
#     )

#     context = {"form": form, "orders": orders}
#     return render(request, "users/profile.html", context)


# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = auth.authenticate(request, username=username, password=password)

#             session_key = request.session.session_key

#             if user:
#                 auth.login(request, user)

#                 if session_key:
#                     Cart.objects.filter(session_key=session_key).update(user=user)
#                 # messages.success(request, f'{username}, вы успешно авторизованы!')
#                 redirect_page = request.POST.get("next", None)
#                 if redirect_page and redirect_page != reverse("users:logout"):
#                     return HttpResponseRedirect(request.POST.get("next"))

#             return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserLoginForm()

#     context = {"form": form}
#     return render(request, "users/login.html", context)


# def registration(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()

#             session_key = request.session.session_key

#             user = form.instance
#             auth.login(request, user)

#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)
#             # messages.success(request, f'{user.username}, вы успешно зарегистрированы!')
#             return HttpResponseRedirect(reverse("main:index"))
#     else:
#         form = UserRegistrationForm()

#     context = {"form": form}
#     return render(request, "users/registration.html", context)
