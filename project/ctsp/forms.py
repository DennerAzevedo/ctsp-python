from django import forms
from .models import Projeto


class ProjetoForm(forms.ModelForm):
    nome = forms.CharField(max_length=Projeto.nome_max_length)
    siga = forms.CharField(widget=forms.HiddenInput(),
                           max_length=Projeto.sigla_max_length)
    data_inicio = forms.DateField(label='date_begin')
    data_final = forms.DateField(label='date_end')

    class Meta:
        model = Projeto
        fields = ('nome', 'data_inicio', 'data_final')
