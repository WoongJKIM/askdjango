# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 01:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
