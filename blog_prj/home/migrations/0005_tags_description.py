# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 07:09
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
