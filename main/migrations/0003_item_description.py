# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170518_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.SlugField(default='', verbose_name='Описание товара'),
            preserve_default=False,
        ),
    ]