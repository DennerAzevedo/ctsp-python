from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=128, null=False)
    project_name_max_length = project_name.max_length
    project_start_date = models.DateField(default=timezone.now, null=True)
    project_final_date = models.DateField(default=timezone.now, null=True)

    def _str_(self):
        return self.project_name_max_length
