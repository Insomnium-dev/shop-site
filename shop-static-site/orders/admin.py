from django.contrib import admin
from orders.models import Order, OrderItem

from orders.models import Order, OrderItem

# Register your models here.


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    search_fields = (
        "payment_on_get",
        "requires_delivery",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "name", "price", "quantity")
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = ("id",)

    readonly_fields = ("created_timestamp",)

    list_filter = (
        "requires_delivery",
        "payment_on_get",
        "status",
        "is_paid",
        "created_timestamp",
    )

    inlines = (OrderItemTabularAdmin,)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "name",
        "created_timestamp",
    )

    search_fields = ("order",)

    readonly_fields = ("created_timestamp",)

    list_filter = (
        "name",
        "created_timestamp",
    )
