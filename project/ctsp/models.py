from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Projeto(models.Model):
    # este ID é adcionado automaticamente pelo python na ação de salvar como PK
    #id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, null=False)
    sigla = models.CharField(max_length=64, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.nome
