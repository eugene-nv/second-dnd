from django.contrib.auth import get_user_model
from django.test import TestCase

from battle.models import BattleResult
from battle.services.services import attack, add_characters_in_battle_result, damage, result, fight
from characters.models import Character

User = get_user_model()


class BattleViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')

        self.character_1 = Character.objects.create(
            race='Полуэльф',
            klass='Плут',

            name='Астарион',
            gender='мужской',
            ideology='Хаотично-доброе',
            portrait='/portrait/Astarion_0.jpeg',

            level=3,
            experience=2600,
            hp=100,
            ac=100,

            strength=30,
            dexterity=30,
            constitution=30,
            intelligence=30,
            wisdom=30,
            charisma=30,

            owner=self.user,
        ),

        self.character_2 = Character.objects.create(
            race='Человек',
            klass='Волшебник',

            name='Гейл',
            gender='мужской',
            ideology='Нейтральное',
            portrait='/portrait/Gale_0.jpeg',

            level=1,
            experience=1,
            hp=1,
            ac=1,

            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,

            owner=self.user,
        ),

    def test_add_characters_in_battle_result(self):
        result = add_characters_in_battle_result(Character, BattleResult)

        party = (result.first_character.name, result.second_character.name)

        self.assertIn('Астарион', party)
        self.assertIn('Гейл', party)

    def test_attack(self):
        battle = add_characters_in_battle_result(Character, BattleResult)
        a = attack(battle.first_character, battle.second_character)

        self.assertEquals(type(a), int)

        ac = (battle.first_character.ac, battle.second_character.ac)
        self.assertIn(100, ac)
        self.assertIn(1, ac)

    def test_damage(self):
        battle = add_characters_in_battle_result(Character, BattleResult)

        d = damage(battle.first_character, battle.second_character)

        self.assertEquals(type(d), int)

        # hp = (battle.first_character.hp, battle.second_character.hp)
        # self.assertNotIn(100, hp)
        # self.assertNotIn(1, hp)

    def test_result(self):
        battle = add_characters_in_battle_result(Character, BattleResult)
        r = result(battle.first_character, battle.second_character)

        self.assertEquals(type(r), str)

    def test_fight(self):
        f = fight(Character, BattleResult)

        self.assertEquals(f, 'Астарион')

        self.assertEquals(Character.objects.get(name='Астарион').experience, 2900)
        self.assertEquals(Character.objects.get(name='Астарион').level, 4)
        self.assertEquals(Character.objects.get(name='Астарион').ac, 100)
        self.assertEquals(Character.objects.get(name='Астарион').hp, 100)

        self.assertEquals(Character.objects.get(name='Гейл').experience, 1)
        self.assertEquals(Character.objects.get(name='Гейл').level, 1)
        self.assertEquals(Character.objects.get(name='Гейл').ac, 1)
        self.assertEquals(Character.objects.get(name='Гейл').hp, 1)


    # def test_fight(self):
    #     r = fight(Character, BattleResult)
    #
    #     self.assertEquals(r, 'Астарион')
    #
    #     self.assertEquals(Character.objects.get(name='Астарион').experience, 2900)
    #     self.assertEquals(Character.objects.get(name='Астарион').level, 4)
    #     self.assertEquals(Character.objects.get(name='Астарион').ac, 100)
    #     self.assertEquals(Character.objects.get(name='Астарион').hp, 100)
    #
    #     self.assertEquals(Character.objects.get(name='Гейл').experience, 1)
    #     self.assertEquals(Character.objects.get(name='Гейл').level, 1)
    #     self.assertEquals(Character.objects.get(name='Гейл').ac, 1)
    #     self.assertEquals(Character.objects.get(name='Гейл').hp, 1)
