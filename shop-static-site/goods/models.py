from email.mime import image
from enum import unique
from os import name
from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length = 150, unique = True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length = 150, unique = True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    price = models.DecimalField(default=0.00, max_digits=7, blank=True, null=True, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(to=Categories,on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        
    def __str__(self):
        return self.name
