# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20170506_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
