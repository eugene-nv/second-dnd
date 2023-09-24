from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from characters.models import Character

User = get_user_model()


class CharacterViewTestCase(TestCase):

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

    def test_home_page(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'home.html')

    def test_battle(self):
        path = reverse('battle')
        response = self.client.get(path)

        hp_first = 6
        hp_second = 8

        attack_first = 3
        attack_second = 4

        # fight(hp_first, hp_second, attack_first, attack_second, self.character_1, self.character_2)

        self.assertEquals(response.status_code, HTTPStatus.OK)

    # def test_create(self):
    #     path = reverse('create', )
    #
    #     data = {
    #             "race": "Полуэльф",
    #             "klass": "Плут",
    #             "name": "Тест",
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
    #     response = self.client.post(path, data=data)
    #
    #     self.assertEquals(response.status_code, HTTPStatus.FOUND)
    #     self.assertRedirects(response, reverse('home'))
    #     self.assertEquals(data['name'], Character.objects.last().name)
    #     self.assertEquals(data['owner'], Character.objects.last().owner.id)
