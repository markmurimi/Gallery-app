# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0012_auto_20180509_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_id',
            field=models.CharField(max_length=30),
        ),
    ]