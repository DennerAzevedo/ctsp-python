from django import forms

class ProjectForm(forms.Form):
	project_name = forms.CharField(label='name', max_length=100)
	date_begin = forms.DateField(label='date_begin')
	date_end = forms.DateField(label='date_end')