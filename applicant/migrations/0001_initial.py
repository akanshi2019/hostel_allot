# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostel', '0005_auto_20180804_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='allot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='hostel.UserProfile')),
            ],
        ),
    ]
