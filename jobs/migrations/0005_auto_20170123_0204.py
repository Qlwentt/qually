# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20170123_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='jobs',
            field=models.ManyToManyField(blank=True, null=True, to='jobs.SavedJob'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yrs_exp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]