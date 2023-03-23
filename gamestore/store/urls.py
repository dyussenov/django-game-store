from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sale/', sale, name='sale'),
    path('game/<int:id>/', game, name='game')
]
