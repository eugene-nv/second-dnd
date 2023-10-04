# from django import forms
#
# from characters.models import Character
#
#
# class SelectForm(forms.Form):
#     heroes = forms.ModelChoiceField(queryset=Character.objects.all())


from django.forms import ModelForm, HiddenInput

from .models import BattleResult


class BattleResultForm(ModelForm):
    class Meta:
        model = BattleResult
        fields = '__all__'
        widgets = {'second_character': HiddenInput(),
                   'result': HiddenInput()
                   }