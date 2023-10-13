import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

# from .tasks import fight
from characters.services.services import character_list, fight
from .forms import BattleResultForm
from characters.models import Character
from .models import BattleResult
from .tasks import fight_task


class SelectViews(CreateView):
    form_class = BattleResultForm
    template_name = 'character_select.html'
    success_url = reverse_lazy('2battle')

    model = BattleResult

    def form_valid(self, form):
        b = BattleResult.objects.last()
        instance = form.save(commit=False)
        instance.second_character = random.choice([i.name for i in character_list if i.name != b.first_character])
        instance.save()
        return super().form_valid(form)


def battle_app(request):
    battle = BattleResult.objects.last()

    fight_task.delay(battle.id)

    context = {
        'first_character': battle.first_character,
        'second_character': battle.second_character,
        'result': battle.result,
        'log': battle.log,
    }


    return render(request, '2battle.html', context)


class ArenaView(ListView):
    template_name = 'arena.html'
    context_object_name = 'result'

    def get_queryset(self):
        return BattleResult.objects.all()
