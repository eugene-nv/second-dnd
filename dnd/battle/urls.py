from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', ArenaView.as_view(), name="arena"),
    path('b', battle_app, name="2battle"),
    path('select', SelectViews.as_view(), name="select"),
    # path('test', select_for_battle, name="select"),



]