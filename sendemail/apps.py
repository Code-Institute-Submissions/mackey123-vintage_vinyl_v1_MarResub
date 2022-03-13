""" send email apps config """
from django.apps import AppConfig


class SendemailConfig(AppConfig):
    """ send email appconfig class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sendemail'
