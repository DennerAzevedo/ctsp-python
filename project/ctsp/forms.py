from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='project_name do Project', max_length=Project.project_name_max_length)
    project_init = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Sigla', max_length=Project.project_init_max_length)
    proiect_start_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class':'control-label m-3', 'id':'from_forms', 'placeholder':"MM/DD/YYY",
        }
    ), label='Start date')
    project_final_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class':'control-label m-3', 'id':'from_forms', 'placeholder':"MM/DD/YYY",
        }
    ), label='Final date')

    class Meta:
        model = Project
        fields = ('project_name', 'project_init', 'proiect_start_date', 'project_final_date',)
