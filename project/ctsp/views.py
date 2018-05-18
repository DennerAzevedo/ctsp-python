from django.shortcuts import render
from .forms import ProjetoForm
from .models import Projeto

# Create your views here.


def index(request):
    form = ProjetoForm()

    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    context_dict = {"form": form}
    return render(request, 'ctsp/index.html', context_dict)


def about(request):
    return render(request, 'ctsp/about.html')


def project_welcome(request):
    return render(request, 'ctsp/about.html')
