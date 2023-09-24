from django.db import models
from django.contrib.auth import get_user_model

from .lib.klasses import *
from .lib.races import *
from .lib.description import *

User = get_user_model()


class Character(models.Model):
    race = models.CharField(max_length=255, choices=RACES, verbose_name='Раса')
    klass = models.CharField(max_length=255, choices=KLASSES, verbose_name='Класс')

    name = models.CharField(max_length=255, verbose_name='Имя')
    gender = models.CharField(max_length=255, choices=GENDER, verbose_name='Пол')
    ideology = models.CharField(max_length=255, choices=IDEOLOGY, verbose_name='Мировоззрение')
    portrait = models.ImageField(upload_to='portrait/', null=True, verbose_name='Портрет')

    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)
    experience = models.IntegerField(verbose_name='Опыт', blank=True, null=True)
    hp = models.IntegerField(verbose_name='Здоровье', blank=True, null=True)
    ac = models.IntegerField(verbose_name='Класс доспехов', blank=True, null=True)

    strength = models.IntegerField(verbose_name='Сила')
    dexterity = models.IntegerField(verbose_name='Ловкость')
    constitution = models.IntegerField(verbose_name='Телосложение')
    intelligence = models.IntegerField(verbose_name='Интеллект')
    wisdom = models.IntegerField(verbose_name='Мудрость')
    charisma = models.IntegerField(verbose_name='Харизма')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.race} - {self.klass} {self.level} уровня'

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
        ordering = ['id']
