#!/usr/bin/env python
# coding: utf-8


from django.urls import path
from . import views
 
urlpatterns = [
    path('callback', views.callback)
]

# from django.urls import path

# from .views import callback

# urlpatterns = [
#     path('callback', callback)
# ]
