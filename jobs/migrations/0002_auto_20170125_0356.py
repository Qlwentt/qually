# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachedjob',
            name='exp_req',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cachedjob',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='jobs.Keyword'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='savedjob',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
