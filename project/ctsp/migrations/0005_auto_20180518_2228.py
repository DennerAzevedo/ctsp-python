# Generated by Django 2.0.5 on 2018-05-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctsp', '0004_auto_20180518_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='sigla',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
