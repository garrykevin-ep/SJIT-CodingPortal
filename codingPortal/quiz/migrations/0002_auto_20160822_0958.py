# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-22 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MECHQuestions',
            new_name='CSEQuestion',
        ),
        migrations.RenameModel(
            old_name='ECEQuestions',
            new_name='ECEQuestion',
        ),
        migrations.RenameModel(
            old_name='CSEQuestions',
            new_name='EEEQuestion',
        ),
        migrations.RenameModel(
            old_name='EEEQuestions',
            new_name='ITQuestion',
        ),
        migrations.RenameModel(
            old_name='ITQuestions',
            new_name='MECHQuestion',
        ),
    ]
