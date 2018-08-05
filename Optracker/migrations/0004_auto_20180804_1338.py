# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-04 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Optracker', '0003_auto_20180804_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optrackertable',
            name='process_Impact',
            field=models.CharField(choices=[('BOOKING', 'Booking'), ('TRAFFICKING', 'Trafficking'), ('REPORTING', 'Reporting'), ('EXPANSION SERVICES', 'Expansion Services')], default=None, max_length=100, null=True),
        ),
    ]