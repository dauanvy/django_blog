# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 06:13
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
