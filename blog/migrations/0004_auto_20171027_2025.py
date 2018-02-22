# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171026_0526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentation',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.RemoveField(
            model_name='time_table',
            name='image2',
        ),
        migrations.AlterField(
            model_name='add_teacher',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='О преподавателе'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 27, 17, 25, 10, 526805, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='file',
            field=models.FileField(upload_to='files/documents', verbose_name='Выберите документ'),
        ),
    ]