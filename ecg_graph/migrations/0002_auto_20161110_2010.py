# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecg_graph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecgdata',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ecgdata',
            name='data_json',
            field=models.TextField(),
        ),
    ]
