from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', CharacterViews.as_view(), name='home'),
    path('characters/', OwnerCharactersViews.as_view(), name='characters'),
    path('characters/<int:pk>/', ShowCharacter.as_view(), name='show_characters'),
    path('characters/<int:pk>/delete/', CharacterDeleteView.as_view(), name='delete_character'),
    path('characters/<int:pk>/update/', CharacterUpdateView.as_view(), name='update_character'),
    path('create/', CreateCharacter.as_view(), name='create'),

    path('vue-list/', list_app, name="list"),
    path('vue-create/', create_app, name="list"),

]