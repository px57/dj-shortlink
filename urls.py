"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'create/', 
        views.create, 
        name='create'
    ),
    path(
        '<str:path>', 
        views.redirect, 
        name='redirect'
    ),
]