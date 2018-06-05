from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    '''
    This class creates our Project model, which is the essential definition of our table fields and behaviour.
    To learn more about MySQL database modeling refer to: https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-creating-a-model.html
    To learn more about Django database models refer to: https://docs.djangoproject.com/en/2.0/topics/db/models/
    '''

    project_name = models.CharField(max_length=128, null=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(default=timezone.now, null=True)
    project_final_date = models.DateField(default=timezone.now, null=True)

    def _str_(self):
        return self.project_name_max_length
    
   
class MembrosDoTime(models.Model):
    membrosDoTime_name = models.CharField(max_length=30, null=False)
    membrosDoTime_name_max_length = membrosDoTime_name.max_length
    membrosDoTime_sobrename = models.CharField(max_lenght=100, null=False)
    membrosDoTime_sobrename_max_length = membrosDoTime_sobrename.max_length
    membrosDoTime_nascimento = models.DataField(default=timezone.now, null = True)
    membrosDoTime_telefone = models.CharField('Telefone para Contato', max_length=13,blank=True, null=True)
    membrosDoTime_habilidades = models.CharField(max_lenght = 300, null = True)
    membrodDoTime_login = models.CharField(max_lenght = 50, null =False)
    membrosDoTime_senha = models.CharField(max_lenght = 100, null = False)
    
    def _str_(self):
        return self.membrosDoTime_name_max_length
