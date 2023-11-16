import random

from characters.services.services import check_level, modifier


# def attack(hero):
#     return modifier(hero.strength) + random.randint(1, 20)
#
#
# def damage(hero):
#     return modifier(hero.strength) + random.randint(1, 6)


def add_characters_in_battle_result(characters_db, battle_db):
    index_list = [i.id for i in characters_db.objects.all()]
    random.shuffle(index_list)

    battle = battle_db.objects.create(first_character=characters_db.objects.get(id=index_list[0]),
                                      second_character=characters_db.objects.get(id=index_list[1]))

    return battle


def attack(attacking, defending):
    return defending.ac - (modifier(attacking.strength) + random.randint(1, 20))


def damage(attacking, defending):
    defending.hp -= modifier(attacking.strength) + random.randint(1, 6)
    d = defending.hp - (modifier(attacking.strength) + random.randint(1, 6))
    defending.save()
    return d


def result(attacking, defending):
    attacking.experience += 300
    attacking.level = check_level(attacking)
    attacking.save()
    return attacking.name


def fight(characters_db, battle_db):
    battle = add_characters_in_battle_result(characters_db, battle_db)

    start_first_hp = battle.first_character.hp
    start_second_hp = battle.second_character.hp

    while battle.first_character.hp >= 0 and battle.second_character.hp >= 0:

        # First character turn

        a1 = attack(battle.first_character, battle.second_character)
        if a1 <= 0:
            d1 = damage(battle.first_character, battle.second_character)
            battle.save()
            if d1 <= 0:
                battle.result = result(battle.first_character, battle.second_character)
                battle.save()
                break

        # Second character turn

        a2 = attack(battle.second_character, battle.first_character)
        if a2 <= 0:
            d2 = damage(battle.second_character, battle.first_character)
            battle.save()
            if d2 <= 0:
                battle.result = result(battle.second_character, battle.first_character)
                battle.save()
                break

    battle.first_character.hp = start_first_hp
    battle.first_character.save()
    battle.second_character.hp = start_second_hp
    battle.second_character.save()
    battle.save()
    return battle.result


#         # First character turn
#
#         f = character_attack(battle.first_character, battle.second_character, log)
#
#         if f <= 0:
#             d1 = character_damage(battle.first_character, battle.second_character, log)
#
#             if d1 <= 0:
#                 r = result(battle.first_character)
#
#                 break


# def start(attacking, defending):
#     return {
#         'first': {
#             'start_ac': attacking.ac,
#             'start_hp': attacking.hp
#         },
#         'second': {
#             'start_ac': defending.ac,
#             'start_hp': defending.hp
#         }
#     }


# def character_attack(attacking, defending, log):
#     defending_ac = defending.ac
#
#     defending.ac = defending_ac
#     attacking_attack = attack(attacking)
#     ac_before_attack = defending.ac
#     defending.ac -= attacking_attack
#     log += f"Атака {attacking.name}: {ac_before_attack} - {attacking_attack} = {defending.ac}>>"
#
#     return defending.ac
#
#
# def character_damage(attacking, defending, log):
#     log += "Попадание>>"
#     attacking_damage = damage(attacking)
#     hp_before_damage = defending.hp
#     defending.hp -= attacking_damage
#     log += f"Урон {attacking.name}: {hp_before_damage} - {attacking_damage} = {defending.hp}>>"
#
#     return defending.hp
#
#
# def result(attacking):
#     res = attacking.name
#     attacking.experience += 300
#     attacking.level = check_level(attacking)

# attacking.hp = sfh
# defending.hp = ssh
#
# attacking.ac = sfa
# defending.ac = ssa
#
# attacking.save()
# defending.save()

# return res


# def fight(characters_db, battle_db):
#     battle = add_characters_in_battle_result(characters_db, battle_db)
#
#     log = ''
#
#     start_first_ac = battle.first_character.ac
#     start_second_ac = battle.second_character.ac
#
#     start_first_hp = battle.first_character.hp
#     start_second_hp = battle.second_character.hp
#
#     while battle.first_character.hp >= 0 and battle.second_character.hp >= 0:
#
#         # First character turn
#
#         f = character_attack(battle.first_character, battle.second_character, log)
#
#         if f <= 0:
#             d1 = character_damage(battle.first_character, battle.second_character, log)
#
#             if d1 <= 0:
#                 r = result(battle.first_character)
#
#                 break
#
#         # Second character turn
#
#         s = character_attack(battle.second_character, battle.first_character, log)
#
#         if s <= 0:
#             d2 = character_damage(battle.second_character, battle.first_character, log)
#
#             if d2 <= 0:
#                 r = result(battle.second_character)
#
#                 break
#         else:
#             log += "Промах>>"
#
#     battle.result = r
#     battle.log = log
#     battle.save()
#
#     return battle.result


def get_log(db):
    return db.log.split(">>")

# def attack(attacking, defending, characters_db, battle_db):
#     battle = add_characters_in_battle_result(characters_db, battle_db)
#     return 1
