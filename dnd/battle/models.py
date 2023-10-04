from django.db import models

from battle.lib.characters import FIRST_CHARACTER
from characters.models import Character


class BattleResult(models.Model):
    first_character = models.CharField(max_length=255, choices=FIRST_CHARACTER, verbose_name='1 Персонаж', blank=True, null=True)
    second_character = models.CharField(max_length=255, verbose_name='2 Персонаж', blank=True, null=True)
    result = models.CharField(max_length=255, verbose_name='Результат', blank=True, null=True)
