# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-02 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
    ]
