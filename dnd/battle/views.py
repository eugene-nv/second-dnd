from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView

from .tasks import random_fight
from characters.services.services import *
from .forms import BattleResultForm
from characters.models import Character
from .models import BattleResult


class SelectViews(CreateView):
    form_class = BattleResultForm
    template_name = 'character_select.html'
    success_url = reverse_lazy('2battle')

    model = BattleResult

    def form_valid(self, form):
        b = BattleResult.objects.last()
        instance = form.save(commit=False)
        second_char_name = random.choice([i.name for i in character_list if i.name != b.first_character])

        instance.second_character = second_char_name

        instance.save()
        return super().form_valid(form)


def random_battle_app(request):
    char_id_list = [i.id for i in character_list]
    random.shuffle(char_id_list)
    characters = char_id_list[:2]

    first_character = Character.objects.get(pk=characters[0])
    second_character = Character.objects.get(pk=characters[1])

    random_fight.delay(first_character, second_character)

    context = {
        'first_character': first_character,
        'second_character': second_character,
        # 'fight': random_fight.delay(first_character, second_character),
    }

    return render(request, 'battle.html', context)


def battle_app(request):
    battle = BattleResult.objects.last()

    first_character = Character.objects.get(name=battle.first_character)
    second_character = Character.objects.get(name=battle.second_character)

    if battle.result:
        f = 'End'
    else:
        f = fight(first_character, second_character)
        battle.result = f['result']
        battle.save()

    context = {
        'first_character': first_character,
        'second_character': second_character,
        'fight': f,
    }

    return render(request, '2battle.html', context)


class ArenaView(ListView):
    template_name = 'arena.html'
    context_object_name = 'result'

    def get_queryset(self):
        return BattleResult.objects.all()