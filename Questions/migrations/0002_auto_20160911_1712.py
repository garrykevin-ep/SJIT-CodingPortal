# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-11 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProgrammingQuestion',
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
        migrations.DeleteModel(
            name='VerbalQuestion',
        ),
    ]
