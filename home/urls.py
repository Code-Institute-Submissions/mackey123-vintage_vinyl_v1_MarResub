""" url route path for home """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
 ]
