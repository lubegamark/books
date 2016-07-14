# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available_at',
            field=models.ManyToManyField(blank=True, null=True, to='books.Source'),
        ),
        migrations.AlterField(
            model_name='book',
            name='chapters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='content_page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='formats',
            field=models.ManyToManyField(blank=True, null=True, related_name='books', to='books.Format'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='searches',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
