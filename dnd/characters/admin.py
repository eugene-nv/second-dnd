from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Character


@admin.register(Character)
class CharacterAdmin(ModelAdmin):
    pass
