# Generated by Django 5.0.1 on 2024-02-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python2_django', '0003_rename_datecreation_sessionsurvey_datestarted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionsurvey',
            name='url',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
