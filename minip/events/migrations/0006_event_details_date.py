# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-30 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170623_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_details',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
