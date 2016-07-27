# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160615_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 14, 12, 15, 26, 820818, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 14, 12, 15, 42, 418241, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='available_at',
            field=models.ManyToManyField(blank=True, to='books.Source'),
        ),
        migrations.AlterField(
            model_name='book',
            name='formats',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.Format'),
        ),
    ]