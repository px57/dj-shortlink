"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_or_get/',
        views.create_or_get,
        name='create_or_get'
    ),
    path(
        'get/',
        views.get,
        name='get'
    ),
]
