# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-20 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20180920_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='room',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
