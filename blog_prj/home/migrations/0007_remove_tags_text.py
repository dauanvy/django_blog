# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tags_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='text',
        ),
    ]
