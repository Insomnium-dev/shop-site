from django.contrib import admin
from orders.models import Order, OrderItem

from orders.models import Order, OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)