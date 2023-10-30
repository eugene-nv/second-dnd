from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [

    # path('', arena, name="arena"),
    # path('battle-result/<int:pk>/', ShowBattleResult.as_view(), name='show_battle_result'),
    path('battle-result/<int:battle_id>/', show_battle_result, name='show_battle_result'),

    path('', ArenaView.as_view(), name="arena"),
    # path('battle/<int:pk>/', ShowBattle.as_view(), name='show_battle'),
    # path('battle/<int:pk>/', show_battle, name='show_battle'),




]