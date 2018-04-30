from django.db import models


# Create your models here.
class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, null=False)
    sigla = models.CharField(max_length=64, null=True)
