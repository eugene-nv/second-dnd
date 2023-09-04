
from django.contrib.auth import get_user_model
from django.test import TestCase

from characters.models import Character
from api.serializers import CharacterSerializer

User = get_user_model()


class CharacterSerializerTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_username')

        character_1 = Character.objects.create(
            race='Полуэльф',
            klass='Плут',
            name='Астарион',
            gender='мужской',
            ideology='Хаотично-доброе',
            portrait='/portrait/Astarion_0.jpeg',
            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,
            owner=self.user,
        )

        character_2 = Character.objects.create(
            race='Человек',
            klass='Волшебник',
            name='Гейл',
            gender='мужской',
            ideology='Нейтральное',
            portrait='/portrait/Gale_0.jpeg',
            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,
            owner=self.user,
        )

        data = CharacterSerializer([character_1, character_2], many=True).data

        expected_data = [
            {
                "id": character_1.id,
                "race": "Полуэльф",
                "klass": "Плут",
                "name": "Астарион",
                "gender": "мужской",
                "ideology": "Хаотично-доброе",
                "portrait": "/media/portrait/Astarion_0.jpeg",
                "strength": 1,
                "dexterity": 1,
                "constitution": 1,
                "intelligence": 1,
                "wisdom": 1,
                "charisma": 1,
                "owner": self.user.id
            },
            {
                "id": character_2.id,
                "race": "Человек",
                "klass": "Волшебник",
                "name": "Гейл",
                "gender": "мужской",
                "ideology": "Нейтральное",
                "portrait": "/media/portrait/Gale_0.jpeg",
                "strength": 1,
                "dexterity": 1,
                "constitution": 1,
                "intelligence": 1,
                "wisdom": 1,
                "charisma": 1,
                "owner": self.user.id
            },
        ]

        self.assertEquals(expected_data, data)
