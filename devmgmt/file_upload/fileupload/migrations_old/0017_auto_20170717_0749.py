# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0016_auto_20170717_0742'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Permissions',
            new_name='Permission',
        ),
    ]
