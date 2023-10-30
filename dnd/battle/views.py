from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView

from characters.models import Character
from .models import BattleResult
from .services.services import get_log


class ArenaView(ListView):
    template_name = 'arena/arena.html'
    context_object_name = 'result'

    def get_queryset(self):
        return BattleResult.objects.all()


def show_battle_result(request, battle_id):
    result = get_object_or_404(BattleResult, pk=battle_id)

    log = get_log(result)

    context = {
        'result': result,
        'log': log,
    }

    return render(request, 'arena/battle_result.html', context=context)
