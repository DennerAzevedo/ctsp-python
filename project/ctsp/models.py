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
