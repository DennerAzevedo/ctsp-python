from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .forms import ProjectForm, QueryProjectForm
from .models import Project

# Create your views here.


def index(request):
    form = ProjectForm()
    query = QueryProjectForm()
    context_dict = {'form': form, 'query': query}

    return render(request, 'ctsp/index.html', context=context_dict)


def create_project_modal(request):
    form = ProjectForm()
    context_dict = {'form': form}

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=True)
            context_dict['project'] = Project.objects.filter(pk=project.pk)
            return render(request, 'ctsp/welcome.html', context=context_dict)
    return render(request, 'ctsp/index.html', context_dict)

def query_project_modal(request):
    query = QueryProjectForm()
    context_dict = {'query': query}
    if request.method == 'POST':
        query = QueryProjectForm(request.POST)
        print(query)

    return render(request, 'ctsp/index.html', context_dict)

def about(request):
    return render(request, 'ctsp/about.html')


def project_welcome(request):
    return render(request, 'ctsp/welcome.html')
