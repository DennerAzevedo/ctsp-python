from django.urls import path
from . import views

app_name = 'ctsp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.create_project_modal, name='create_project_modal'),
    path('###/', views.query_project_modal, name='query_project_modal'),
]
