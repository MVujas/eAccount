# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Neto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('pay', models.IntegerField()),
                ('status', models.CharField(default=b'Active', max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Radnik',
        ),
    ]
