# Generated by Django 2.0.5 on 2018-05-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctsp', '0008_auto_20180519_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=128),
        ),
    ]
