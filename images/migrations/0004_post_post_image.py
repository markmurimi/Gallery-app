# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20180506_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default=1, upload_to='posts/'),
            preserve_default=False,
        ),
    ]
