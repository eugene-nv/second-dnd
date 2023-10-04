from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BattleResult


@admin.register(BattleResult)
class BattleResultAdmin(ModelAdmin):
    pass

