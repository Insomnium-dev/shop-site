# from django.db import models

# # Create your models here.
# from django.db import models

# # Create your models here.


# class Cart(models.Model):
#     name = models.CharField(max_length = 150, unique = True, verbose_name="Название")
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
#     price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
#     image = models.ImageField(upload_to="goods_images",blank=True, null=True, verbose_name="Изображение")
#     description = models.TextField(max_length=1000,unique=True,blank=True,null=True,verbose_name="Описание")
#     discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %")

#     class Meta:
#         db_table = "product"
#         verbose_name = "Продукт"
#         verbose_name_plural = "Продукты"
        
#     def __str__(self):
#         return self.name
    
#     def display_id(self):
#         return f"{self.id:05}"
    
#     def calc_discount(self):
#         if self.discount:
#             return format(self.price - self.price*self.discount/100,'.2f')