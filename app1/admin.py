from django.contrib import admin

# Register your models here.
from .models import Product,Cart,Glasses,WGlasses

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Glasses)
admin.site.register(WGlasses)
