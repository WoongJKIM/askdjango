# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 16, 0, 45, 56, 984012, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
