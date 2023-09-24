from django import forms

from characters.models import Character


class SelectForm(forms.Form):
    heroes = forms.ModelChoiceField(queryset=Character.objects.all())
