from django.contrib.auth import get_user_model
from django.test import TestCase

from battle.models import BattleResult
from battle.services.services import fight
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

    def test_fight(self):
        result = fight(Character, BattleResult)

        self.assertEquals(result, 'Астарион')

        self.assertEquals(Character.objects.get(name='Астарион').experience, 2900)
        self.assertEquals(Character.objects.get(name='Астарион').level, 4)
        self.assertEquals(Character.objects.get(name='Астарион').ac, 100)
        self.assertEquals(Character.objects.get(name='Астарион').hp, 100)

        self.assertEquals(Character.objects.get(name='Гейл').experience, 1)
        self.assertEquals(Character.objects.get(name='Гейл').level, 1)
        self.assertEquals(Character.objects.get(name='Гейл').ac, 1)
        self.assertEquals(Character.objects.get(name='Гейл').hp, 1)
