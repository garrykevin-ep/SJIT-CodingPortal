# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0012_auto_20160906_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='Department',
            field=models.CharField(choices=[(1, 'CSE'), (2, 'CIVIL'), (3, 'EEE'), (4, 'ECE'), (5, 'IT'), (6, 'MECH')], max_length=200),
        ),
    ]
