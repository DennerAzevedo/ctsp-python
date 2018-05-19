from django.contrib import admin
from ctsp.models import Project

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Information", {"fields": [
            'id', "name", 'init', 'start_date', 'final_date']}),
    ]
    list_display = ('id', "name", 'init', 'start_date', 'final_date')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', "project_name", 'project_init', 'project_start_date', 'project_final_date')


admin.site.register(Project, ProjectAdmin)
