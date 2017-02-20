# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20170209_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('avatar', models.CharField(default='static/images/default.png', max_length=250)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createdate', models.DateField(auto_now=True)),
                ('createtime', models.TimeField(auto_now=True)),
                ('belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='firstapp.Article')),
            ],
        ),
    ]