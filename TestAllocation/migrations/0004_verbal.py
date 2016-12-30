# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-29 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestAllocation', '0003_auto_20161227_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verbal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestName', models.CharField(max_length=200)),
                ('VerbalTagName', models.IntegerField(choices=[(1, 'Comprehension'), (3, 'Time and Work'), (4, 'Profit and Loss')], verbose_name='Verbal Tags')),
                ('StartDate', models.DateField(blank=True, verbose_name='Start Date')),
                ('StartTime', models.TimeField(blank=True, verbose_name='Start Time')),
                ('EndDate', models.DateField(blank=True, verbose_name='End Date')),
                ('EndTime', models.TimeField(blank=True, verbose_name='End Time')),
                ('Batch', models.IntegerField(choices=[(1, '2013-2017'), (2, '2014-2018'), (3, '2015-2019'), (4, '2016-2020')])),
                ('Department', models.IntegerField(choices=[(1, 'CSE'), (2, 'EEE'), (3, 'ECE'), (4, 'IT'), (5, 'MECH'), (6, 'CIVIL')])),
            ],
            options={
                'verbose_name': 'Verbal',
                'verbose_name_plural': 'Verbal',
            },
        ),
    ]