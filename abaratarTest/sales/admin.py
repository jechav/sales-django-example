from django.contrib import admin
from .models import Product, Sale, Client

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
