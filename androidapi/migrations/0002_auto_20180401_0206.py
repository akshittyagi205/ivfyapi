# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-31 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androidapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='aadhaarOwner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='businessId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='businessaddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='businessname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='businesstype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='required',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ekycbusiness',
            name='businessId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ekycbusiness',
            name='data',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='datacreater',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='datajoiner',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='sessionId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]