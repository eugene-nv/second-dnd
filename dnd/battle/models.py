from django.db import models

from characters.models import Character


class BattleResult(models.Model):
    first_character = models.ForeignKey(to=Character, on_delete=models.CASCADE, related_name='first', null=True, blank=True)
    second_character = models.ForeignKey(to=Character, on_delete=models.CASCADE, related_name='second', null=True, blank=True)
    result = models.CharField(max_length=255, verbose_name='Результат', blank=True, null=True)
    log = models.TextField(verbose_name='Лог', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)



