# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-04 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_remove_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='choice',
            field=models.CharField(default=0, max_length=20),
        ),
    ]