from django.contrib import admin
from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass