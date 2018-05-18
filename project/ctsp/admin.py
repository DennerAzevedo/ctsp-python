from django.contrib import admin
from ctsp.models import Projeto

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Information", {"fields": [
         "nome", 'sigla', 'data_inicio', 'data_final']}),
    ]
    list_display = ('nome', 'sigla', 'data_inicio', 'data_final')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'data_inicio', 'data_final')

admin.site.register(Projeto, ProjetoAdmin)