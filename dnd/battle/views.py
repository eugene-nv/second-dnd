from django.shortcuts import render, redirect
import random

from django.views import View

from characters.services.services import *
from .forms import SelectForm
from characters.models import Character


class SelectViews(View):
    template_name = 'character_select.html'
    form = SelectForm()

    def get(self, request):
        context = {
            'select': self.form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = SelectForm(request.POST)

        context = {
            'm': form,
        }

        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return redirect('home')

        return render(request, self.template_name, context)


def battle_app(request):
    char_id_list = [i.id for i in character_list]
    random.shuffle(char_id_list)
    characters = char_id_list[:2]

    first_character = Character.objects.get(pk=characters[0])
    second_character = Character.objects.get(pk=characters[1])

    context = {
        'first_character': first_character,
        'second_character': second_character,
        'fight': fight(first_character, second_character),
    }

    return render(request, 'battle.html', context)
