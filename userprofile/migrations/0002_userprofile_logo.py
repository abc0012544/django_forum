# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-01 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='logo',
            field=models.CharField(blank=True, max_length=300, verbose_name='头像'),
        ),
    ]
