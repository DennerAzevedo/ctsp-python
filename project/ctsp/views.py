from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import ProjectForm, QueryProjectForm
from .models import Project


# Create your views here.


class IndexView(TemplateView):
    template_name = 'ctsp/index.html'

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            def ajax_query(request, *args, **kwargs):
                search = request.POST.get('search')
                project_name = Project.objects.filter(project_name__icontains=search)
                project_init = Project.objects.filter(project_init__icontains=search)
                project = max([project_init, project_name], key=len)
                context = []
                for i in range(0, len(project)):
                    context.append({
                        'project_name': project[i].project_name,
                        'project_init': project[i].project_init,
                        'project_start': project[i].project_start_date,
                        'project_end': project[i].project_final_date,
                    })
                return JsonResponse(context, safe=False)

            return ajax_query(self.request, *args, **kwargs)

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
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AboutView(TemplateView):
    template_name = 'ctsp/about.html'
