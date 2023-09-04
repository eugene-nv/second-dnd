import json

from django.contrib.auth import get_user_model

from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase

from characters.models import Character
from api.serializers import CharacterSerializer

User = get_user_model()


class CharacterApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')

        self.character_1 = Character.objects.create(
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
        ),

        self.character_2 = Character.objects.create(
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
        ),

        self.character_3 = Character.objects.create(
            race='Полуэльф',
            klass='Жрец',
            name='Шэдоухарт',
            gender='женский',
            ideology='Хаотично-доброе',
            portrait='/portrait/Shadowheart_0.jpeg',
            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,
            owner=self.user,
        )

    def test_get(self):
        url = reverse('character-list')
        response = self.client.get(url)
        # serializer_data = CharacterSerializer([self.character_1, self.character_2, self.character_3], many=True).data

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        # self.assertEquals(serializer_data, response.data)

    # def test_post(self):
    #     self.assertEquals(3, Character.objects.all().count())
    #
    #     url = reverse('character-list')
    #     data = {
    #             "race": "Полуэльф",
    #             "klass": "Плут",
    #             "name": "Астарион",
    #             "gender": "мужской",
    #             "ideology": "Хаотично-доброе",
    #             "portrait": "/media/portrait/Astarion_0.jpeg",
    #             "strength": 1,
    #             "dexterity": 1,
    #             "constitution": 1,
    #             "intelligence": 1,
    #             "wisdom": 1,
    #             "charisma": 1,
    #             "owner": self.user.id
    #         }
    #
    #     self.client.force_login(self.user)
    #
    #     json_data = json.dumps(data)
    #     response = self.client.post(url, data=json_data,
    #                                 content_type='application/json')
    #
    #     self.assertEquals(status.HTTP_201_CREATED, response.status_code)
    #     self.assertEquals(4, Character.objects.all().count())
    #     self.assertEquals(self.user, Character.objects.last().owner)
