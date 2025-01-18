from django import template

from goods.models import Categories, Products

register=template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_products():
    return Products.objects.all()