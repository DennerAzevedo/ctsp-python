from django import forms
from .models import Projeto


class ProjetoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Nome do Projeto', max_length=Projeto.nome_max_length)
    sigla = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Sigla', max_length=Projeto.sigla_max_length)
    data_inicio = forms.DateField(widget=forms.DateInput(
        attrs={
            'class':'control-label m-3', 'id':'from_forms', 'placeholder':"MM/DD/YYY",
        }
    ), label='Data de início')
    data_final = forms.DateField(widget=forms.DateInput(
        attrs={
            'class':'control-label m-3', 'id':'from_forms', 'placeholder':"MM/DD/YYY",
        }
    ), label='Data final')

    class Meta:
        model = Projeto
        fields = ('nome', 'sigla', 'data_inicio', 'data_final',)
