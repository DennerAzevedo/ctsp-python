from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import ProjectForm, QueryProjectForm
from .models import Project


# Create your views here.


class IndexView(TemplateView):
    template_name = 'ctsp/index.html'

    def get_context_data(self, **kwargs):
        form = ProjectForm()
        query = QueryProjectForm()
        context = super().get_context_data(**kwargs)
        context = {'form': form, 'query': query}
        return context


class ProjectWelcomeView(View):
    form_class = ProjectForm
    context = {}
    template_name = 'ctsp/index.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            project = form.save(commit=True)
            self.context['project'] = Project.objects.filter(pk=project.pk)
            return render(request, 'ctsp/welcome.html', context=self.context)
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


class QueryView(View):
    def get(self, request):
        search = request.GET.get('project_name')
        data = {
            'is_taken': Project.objects.filter(project_name__exact=search).exists()
        }
        print(data)
        return JsonResponse(data)


class AboutView(TemplateView):
    template_name = 'ctsp/about.html'
