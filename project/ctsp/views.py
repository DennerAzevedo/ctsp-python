from django.shortcuts import render
from .forms import ProjectForm

# Create your views here.
def index(request):
	return render(request, 'ctsp/index.html')

def about(request):
	return render(request, 'ctsp/about.html')

def project_welcome(request):
	return render(request, 'ctsp/about.html')

def create_project(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = ProjectForm()
	return render(request, 'ctsp/create_project.html', {'form': form})
