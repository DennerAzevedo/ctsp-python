from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ctsp/index.html')

def about(request):
    return render(request, 'ctsp/about.html')

def project_welcome(request):
    return render(request, 'ctsp/about.html')