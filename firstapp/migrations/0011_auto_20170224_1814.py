# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20170222_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('normal', 'normal'), ('dislike', 'dislike')], max_length=10),
        ),
    ]
