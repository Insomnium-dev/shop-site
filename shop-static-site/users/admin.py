from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email']
    search_display = ['username','first_name', 'last_name', 'email']

    inlines =[
        CartTabAdmin,
    ]

