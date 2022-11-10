from django.contrib import admin

#из ecommerce-project/shop(app)/models.py импортировали наши классы
from .models import Category
from .models import Product


# Register your models here.
#Регистрируем наши моедели
admin.site.register(Category)
admin.site.register(Product)