# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='status',
            field=models.CharField(choices=[('NP', 'Not Played'), ('IP', 'In Progress'), ('CP', 'Completed')], default='NP', max_length=2),
        ),
    ]
