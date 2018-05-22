from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Project Name', max_length=Project.project_name_max_length)
    proiect_start_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'control-label m-3', 'id': 'from_forms', 'placeholder': "MM/DD/YYY",
        }
    ), label='Start date')
    project_final_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'control-label m-3', 'id': 'from_forms', 'placeholder': "MM/DD/YYY",
        }
    ), label='Final date')

    class Meta:
        model = Project
        fields = ('project_name', 'proiect_start_date', 'project_final_date',)


class QueryProjectForm(forms.ModelForm):
    project_name_or_ID = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'id': 'project_name_or_ID'
        }
    ), label='Project Name or ID', max_length=Project.project_name_max_length)

    class Meta:
        model = Project
        fields = ('project_name_or_ID',)
