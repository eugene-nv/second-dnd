from django.forms import ModelForm, HiddenInput

from .models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        widgets = {'owner': HiddenInput(),
                   'level': HiddenInput(),
                   'experience': HiddenInput(),
                   'hp': HiddenInput(),
                   'ac': HiddenInput(),
                   }