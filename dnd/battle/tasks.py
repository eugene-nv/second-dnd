import random
import time

from celery import shared_task
from celery import app

from celery_app import app
from characters.models import Character
from characters.services.services import attack, check_level, damage, start_ac, start_hp, character_list, fight
from .models import BattleResult

char_id_list = [i.id for i in character_list]
random.shuffle(char_id_list)
characters = char_id_list[:2]

first_character = Character.objects.get(pk=characters[0])
second_character = Character.objects.get(pk=characters[1])


# @app.task
# def fight(f, s):
#     from battle.models import BattleResult
#
#     # f = Character.objects.get(name=BattleResult.first_character)
#     # s = Character.objects.get(name=BattleResult.second_character)
#     log = ''
#     result = None
#
#     BattleResult.result = s.name
#     BattleResult.log = log
#
#     start_1_ac = start_ac(f)
#     start_2_ac = start_ac(s)
#
#     start_1_hp = start_hp(f)
#     start_2_hp = start_hp(s)
#
#     while f.hp >= 0 and s.hp >= 0:
#
#         # First character turn
#
#         s.ac = start_2_ac
#         attak_f = attack(f)
#         ac_befor_attack = s.ac
#         s.ac -= attak_f
#         log += f'Атака {f.name}: {ac_befor_attack} - {attak_f} = {s.ac}>>'
#
#         if s.ac <= 0:
#             log += 'Попадание>>'
#             dammage_f = damage(f)
#             hp_befor_dammage = s.hp
#             s.hp -= dammage_f
#             log += f'Урон {f.name}: {hp_befor_dammage} - {dammage_f} = {s.hp}>>'
#
#             if s.hp <= 0:
#                 BattleResult.result = s.name
#                 BattleResult.log = log
#                 f.experience += 300
#                 f.level = check_level(s)
#
#                 f.hp = start_1_hp
#                 s.hp = start_2_hp
#
#                 f.ac = start_1_ac
#                 s.ac = start_2_ac
#
#                 f.save()
#                 s.save()
#
#                 # BattleResult.result.save()
#                 break
#         else:
#             log += 'Промах>>'
#
#         # Second character turn
#
#         f.ac = start_1_ac
#         attak_s = attack(s)
#         ac_befor_attack = f.ac
#         f.ac -= attak_s
#         log += f'Атака {s.name}: {ac_befor_attack} - {attak_s} = {f.ac}>>'
#
#         if f.ac <= 0:
#             log += 'Попадание>>'
#             dammage_s = damage(s)
#             hp_befor_dammage = f.hp
#             f.hp -= dammage_s
#             log += f'Урон {s.name}: {hp_befor_dammage} - {dammage_s} = {f.hp}>>'
#
#             if f.hp <= 0:
#                 BattleResult.result = s.name
#                 # BattleResult.result.save()
#                 BattleResult.log = log
#                 s.experience += 300
#                 s.level = check_level(s)
#
#                 f.hp = start_1_hp
#                 s.hp = start_2_hp
#
#                 f.ac = start_1_ac
#                 s.ac = start_2_ac
#
#                 f.save()
#                 s.save()
#
#                 break
#         else:
#             log += ' >>'


@app.task
def fight_task(id):

    battle = BattleResult.objects.get(id=id)

    f = Character.objects.get(name=battle.first_character)
    s = Character.objects.get(name=battle.second_character)

    log = []
    result = None

    start_1_ac = start_ac(f)
    start_2_ac = start_ac(s)

    start_1_hp = start_hp(f)
    start_2_hp = start_hp(s)

    while f.hp >= 0 and s.hp >= 0:

        # First character turn

        s.ac = start_2_ac
        attak_f = attack(f)
        ac_befor_attack = s.ac
        s.ac -= attak_f
        log.append(f'Атака {f.name}: {ac_befor_attack} - {attak_f} = {s.ac}>>')

        if s.ac <= 0:
            log.append('Попадание>>')
            dammage_f = damage(f)
            hp_befor_dammage = s.hp
            s.hp -= dammage_f
            log.append(f'Урон {f.name}: {hp_befor_dammage} - {dammage_f} = {s.hp}>>')

            if s.hp <= 0:
                result = f.name
                f.experience += 300
                f.level = check_level(s)

                f.hp = start_1_hp
                s.hp = start_2_hp

                f.ac = start_1_ac
                s.ac = start_2_ac

                f.save()
                s.save()

                break
        else:
            log.append('Промах>>')

            # Second character turn

            f.ac = start_1_ac
            attak_s = attack(s)
            ac_befor_attack = f.ac
            f.ac -= attak_s
            log.append(f'Атака {s.name}: {ac_befor_attack} - {attak_s} = {f.ac}>>')

            if f.ac <= 0:
                log.append('Попадание>>')
                dammage_s = damage(s)
                hp_befor_dammage = f.hp
                f.hp -= dammage_s
                log.append(f'Урон {s.name}: {hp_befor_dammage} - {dammage_s} = {f.hp}>>')

                if f.hp <= 0:
                    result = s.name

                    s.experience += 300
                    s.level = check_level(s)

                    f.hp = start_1_hp
                    s.hp = start_2_hp

                    f.ac = start_1_ac
                    s.ac = start_2_ac

                    f.save()
                    s.save()

                    break
            else:
                log.append(' >>')

    battle.result = result
    battle.log = log
    battle.save()

