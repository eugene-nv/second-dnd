from django.db import models
from django.urls import reverse

from battle.lib.characters import FIRST_CHARACTER
from characters.models import Character


class BattleResult(models.Model):
    first_character = models.CharField(max_length=255, choices=FIRST_CHARACTER, verbose_name='1 Персонаж', blank=True, null=True)
    second_character = models.CharField(max_length=255, verbose_name='2 Персонаж', blank=True, null=True)

    # first_character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # second_character = models.CharField(max_length=255, verbose_name='2 Персонаж', blank=True, null=True)

    result = models.CharField(max_length=255, verbose_name='Результат', blank=True, null=True)
    log = models.TextField(verbose_name='Лог', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


