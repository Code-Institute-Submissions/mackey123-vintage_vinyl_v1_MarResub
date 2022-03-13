""" admin model list display """
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """ list display """
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
