# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0018_permission_delete_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='up_from_dev',
            field=models.BooleanField(default=True),
        ),
    ]
