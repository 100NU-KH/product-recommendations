from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_image', 'description',
                    'category', 'price')

admin.site.register(Product, ProductAdmin)