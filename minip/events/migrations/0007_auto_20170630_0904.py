# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-30 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_details_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_details',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
