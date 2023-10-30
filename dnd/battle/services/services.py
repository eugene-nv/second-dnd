import random

from characters.services.services import check_level, modifier


def attack(hero):
    return modifier(hero.strength) + random.randint(1, 20)


def damage(hero):
    return modifier(hero.strength) + random.randint(1, 6)


def add_characters_in_battle_result(characters_db, battle_db):
    index_list = [i.id for i in characters_db.objects.all()]
    random.shuffle(index_list)

    b = battle_db.objects.create(first_character=characters_db.objects.get(id=index_list[0]),
                                 second_character=characters_db.objects.get(id=index_list[1]))

    return b


def fight(characters_db, battle_db):
    battle = add_characters_in_battle_result(characters_db, battle_db)

    log = ''
    result = None

    start_first_ac = battle.first_character.ac
    start_second_ac = battle.second_character.ac

    start_first_hp = battle.first_character.hp
    start_second_hp = battle.second_character.hp

    while battle.first_character.hp >= 0 and battle.second_character.hp >= 0:

        # First character turn

        battle.second_character.ac = start_second_ac
        attack_f = attack(battle.first_character)
        ac_before_attack = battle.second_character.ac
        battle.second_character.ac -= attack_f
        log += f"Атака {battle.first_character.name}: {ac_before_attack} - {attack_f} = {battle.second_character.ac}>>"

        if battle.second_character.ac <= 0:
            log += "Попадание>>"
            damage_f = damage(battle.first_character)
            hp_before_damage = battle.second_character.hp
            battle.second_character.hp -= damage_f
            log += f"Урон {battle.first_character.name}: {hp_before_damage} - {damage_f} = {battle.second_character.hp}>>"

            if battle.second_character.hp <= 0:
                result = battle.first_character.name
                battle.first_character.experience += 300
                battle.first_character.level = check_level(battle.first_character)

                battle.first_character.hp = start_first_hp
                battle.second_character.hp = start_second_hp

                battle.first_character.ac = start_first_ac
                battle.second_character.ac = start_second_ac

                battle.second_character.save()
                battle.first_character.save()

                break

        # Second character turn

        battle.first_character.ac = start_first_ac
        attack_s = attack(battle.second_character)
        ac_before_attack = battle.first_character.ac
        battle.first_character.ac -= attack_s
        log += f"Атака {battle.second_character.name}: {ac_before_attack} - {attack_s} = {battle.first_character.ac}>>"

        if battle.first_character.ac <= 0:
            log += "Попадание>>"
            damage_s = damage(battle.second_character)
            hp_before_damage = battle.first_character.hp
            battle.first_character.hp -= damage_s
            log += f"Урон {battle.second_character.name}: {hp_before_damage} - {damage_s} = {battle.first_character.hp}>>"

            if battle.first_character.hp <= 0:
                result = battle.second_character.name

                battle.second_character.experience += 300
                battle.second_character.level = check_level(battle.second_character)

                battle.first_character.hp = start_first_hp
                battle.second_character.hp = start_second_hp

                battle.first_character.ac = start_first_ac
                battle.second_character.ac = start_second_ac

                battle.second_character.save()
                battle.first_character.save()

                break
        else:
            log += "Промах>>"

    battle.result = result
    battle.log = log
    battle.save()

    return result


def get_log(db):

    return db.log.split(">>")