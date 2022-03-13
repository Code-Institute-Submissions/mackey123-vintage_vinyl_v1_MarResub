""" products app.config """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ product app config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
