# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0003_auto_20160906_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='Batch',
            field=models.CharField(default=-3, max_length=200),
            preserve_default=False,
        ),
    ]