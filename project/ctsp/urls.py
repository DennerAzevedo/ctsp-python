from django.urls import path

from . import views
app_name = 'ctsp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project_welcome/', views.project_welcome, name='project_welcome')
]