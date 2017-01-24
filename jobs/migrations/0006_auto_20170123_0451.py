# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20170123_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('snippet', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='savedjob',
            name='num_keywords',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobs',
            field=models.ManyToManyField(blank=True, to='jobs.SavedJob'),
        ),
    ]