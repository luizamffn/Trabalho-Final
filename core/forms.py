from django import forms
from .models import *

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ('pergunta', 'a', 'b', 'c', 'd', 'correta')