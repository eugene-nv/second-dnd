from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', battle_app, name="battle"),
    path('select', SelectViews.as_view(), name="select"),


]