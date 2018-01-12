# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BlogUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=256)),
                ('password', models.CharField(default='', max_length=256)),
            ],
            options={
                'db_table': 'blogusers',
                'ordering': ['-id'],
            },
        ),
    ]