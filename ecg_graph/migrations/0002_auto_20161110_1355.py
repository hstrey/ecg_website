# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-10 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecg_graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecgdata',
            name='data_json',
            field=models.TextField(),
        ),
    ]
