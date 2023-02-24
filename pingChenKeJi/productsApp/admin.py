from django.contrib import admin
from .models import Product, ProductImg

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImg)