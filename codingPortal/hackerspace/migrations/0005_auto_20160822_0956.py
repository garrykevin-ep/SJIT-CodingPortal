# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-22 04:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='CodingQuestions',
        ),
    ]
