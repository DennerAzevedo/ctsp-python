from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, RedirectView
from django.views.generic.base import ContextMixin, View

from .forms import ProjectForm, QueryProjectForm
from .models import Project


# Create your views here.

class IndexView(View):
    template_name = 'ctsp/index.html'

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            search = request.POST.get('search')
            print(search)

            def is_number(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    return False

            if is_number(search) == True:
                project = Project.objects.filter(id=search)
            else:
                project = Project.objects.filter(project_name__icontains=search)
            context = []
            for i in range(0, len(project)):
                context.append({
                    'project_pk': project[i].id,
                    'project_name': project[i].project_name,
                    'project_start': project[i].project_start_date,
                    'project_end': project[i].project_final_date,
                })
        return JsonResponse(context, safe=False)

    def get(self, request, *args):
        form = ProjectForm()
        query = QueryProjectForm()
        context = {'form': form, 'query': query}
        return render(request, self.template_name, context)


class CreateProjectView(RedirectView):
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=True)
            return redirect('ctsp:project_welcome', pk=project.pk, permanent=False)


class WelcomeProjectView(TemplateView):
    template_name = 'ctsp/welcome_created.html'

    def get_context_data(self, **kwargs):
        context = super(WelcomeProjectView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.filter(pk=context['pk'])
        return context


class AboutView(TemplateView):
    template_name = 'ctsp/about.html'
