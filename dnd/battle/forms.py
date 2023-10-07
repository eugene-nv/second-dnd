from django.forms import ModelForm, HiddenInput

from .models import BattleResult


class BattleResultForm(ModelForm):
    class Meta:
        model = BattleResult
        fields = '__all__'
        widgets = {'second_character': HiddenInput(),
                   'result': HiddenInput(),
                   'log': HiddenInput(),
                   }