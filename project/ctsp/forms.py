from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Project
from django.contrib import messages


class ProjectForm(forms.ModelForm, forms.Form):
    project_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Project Name', max_length=Project.project_name_max_length)
    project_start_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control control-label', 'id': 'start_date', 'placeholder': "MM/DD/YYY",
            'autocomplete': 'off',
        }
    ), label='Start date')
    project_final_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control control-label', 'id': 'final_date', 'placeholder': "MM/DD/YYY", 'autocomplete': 'off',
        }
    ), label='Final date')

    class Meta:
        model = Project
        fields = '__all__'

    # works...
    # def clean_project_name(self):
    #     super().clean()['project_name'] = "aaaaaaaaaaaaaa"
    #     return super().clean()['project_name']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('project_start_date')
        final_date = cleaned_data.get('project_final_date')
        if start_date and final_date:
            if final_date < start_date:
                raise forms.ValidationError("string error")
            return cleaned_data


class QueryProjectForm(forms.ModelForm):
    project_name_or_ID = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'id': 'project_name_or_ID'
        }
    ), label='Project Name or ID', max_length=Project.project_name_max_length)

    class Meta:
        model = Project
        fields = ('project_name_or_ID',)
