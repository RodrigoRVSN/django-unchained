from django.contrib import admin
from .models import Client, Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'stock')

admin.site.register(Client)
admin.site.register(Product, ProductAdmin)