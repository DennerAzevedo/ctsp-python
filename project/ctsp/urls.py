from django.urls import path
from . import views

app_name = 'ctsp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('welcome/', views.CreateProjectView.as_view(), name='create_project'),
    path('welcome_created/<int:pk>/', views.WelcomeProjectView.as_view(), name='project_welcome'),
    path('about/', views.AboutView.as_view(), name='about')
]
