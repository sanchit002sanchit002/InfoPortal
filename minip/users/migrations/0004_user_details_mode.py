# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_details_font'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='mode',
            field=models.CharField(choices=[('1', 'Awaiting'), ('2', 'No'), ('3', 'Yes')], default=1, max_length=1),
        ),
    ]
