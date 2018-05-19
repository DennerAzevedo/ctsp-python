from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import ProjectForm
from .models import Project

# Create your views here.


def index(request):
    form = ProjectForm()
    context_dict = {'form': form}

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=True)
            context_dict['project'] = Project.objects.filter(pk=project.pk)
            print(project.pk)
            return render(request, 'ctsp/project_welcome.html', context_dict)
            # return HttpResponseRedirect(reverse('ctsp:project_welcome', args=(project.pk,)))
    else:
        print(form.errors)
    return render(request, 'ctsp/index.html', context_dict)


def about(request):
    return render(request, 'ctsp/about.html')


def project_welcome(request):
    return render(request, 'ctsp/project_welcome.html')
