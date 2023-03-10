from django import forms

from .models import *

class Tarefaforms(forms.ModelForm):
    titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Adicione uma tarefa...'}))

    class Meta:
        model = Tarefa
        fields = '__all__'