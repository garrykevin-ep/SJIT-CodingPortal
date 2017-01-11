# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-10 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestAllocation', '0005_auto_20161229_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='QuizTagName',
            field=models.IntegerField(choices=[(3, 'Time and Work'), (4, 'Profit and Loss'), (4, 'Syllogism'), (5, 'Arithmetic Reasoning'), (6, 'Series Completion')], verbose_name='Quiz Tags'),
        ),
        migrations.AlterField(
            model_name='verbal',
            name='VerbalTagName',
            field=models.IntegerField(choices=[(4, 'Syllogism'), (5, 'Arithmetic Reasoning'), (6, 'Series Completion')], verbose_name='Verbal Tags'),
        ),
    ]
