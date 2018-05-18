from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Projeto(models.Model):
    # este ID é adcionado automaticamente pelo python na ação de salvar como PK
    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, null=False)
    nome_max_length = nome.max_length
    sigla = models.CharField(max_length=64, null=True)
    sigla_max_length = nome.max_length
    data_inicio = models.DateTimeField(default=timezone.now, null=True)
    data_final = models.DateTimeField(default=timezone.now, null=True)

    def _str_(self):
        return self.nome
