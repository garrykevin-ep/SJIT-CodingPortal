# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-06 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestName', models.CharField(max_length=200)),
                ('TagName', models.CharField(choices=[(1, 'Arrays'), (2, 'Strings'), (3, 'Dynamic Programming')], max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='subCategory',
            field=models.CharField(choices=[(1, 'Arrays'), (2, 'Strings'), (3, 'Dynamic Programming')], max_length=200),
        ),
        migrations.AlterField(
            model_name='verbal',
            name='subCategory',
            field=models.CharField(choices=[(1, 'Arrays'), (2, 'Strings'), (3, 'Dynamic Programming')], max_length=200),
        ),
    ]