from time import sleep

from battle.services.services import fight
from celery_app import app


@app.task
def random_fight_task():
    from battle.models import BattleResult
    from characters.models import Character
    fight(Character, BattleResult)
    sleep(12)
    fight(Character, BattleResult)
    sleep(12)
    fight(Character, BattleResult)
    sleep(12)
    fight(Character, BattleResult)
    sleep(12)
    fight(Character, BattleResult)
