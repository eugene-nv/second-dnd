from django.db.models.signals import post_save
from django.dispatch import receiver

from characters.models import Character


@receiver(post_save, sender=Character)
def post_save_user(**kwargs):
    print('Персонаж изменен')