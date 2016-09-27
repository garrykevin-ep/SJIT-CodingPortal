# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-12 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_auto_20160912_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmingquestion',
            name='subCategory',
            field=models.IntegerField(choices=[(3, 'Arrays'), (4, 'Strings')], max_length=200),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='subCategory',
            field=models.IntegerField(choices=[(3, 'Time and Work'), (4, 'Profit and Loss')], max_length=200),
        ),
        migrations.AlterField(
            model_name='verbalquestion',
            name='subCategory',
            field=models.IntegerField(choices=[(1, 'Comprehension')], max_length=200),
        ),
    ]
