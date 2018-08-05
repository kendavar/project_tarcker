# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-04 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='optrackertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_idea', models.CharField(choices=[('PROCESS', 'Process'), ('TOOL', 'Tool')], default=None, max_length=10)),
                ('problem_statement', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(default=None, null=True)),
                ('description', models.TextField(max_length=10000)),
                ('assign_to', models.CharField(default=None, max_length=100, null=True)),
                ('severity', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default=None, max_length=100)),
                ('Other_tool', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('process_Impact', models.CharField(choices=[('BOOKING', 'Booking'), ('TRAFFICKING', 'Trafficking'), ('REPORTING', 'Reporting'), ('EXPANSION SERVICES', 'Expansion Services')], default=None, max_length=100)),
                ('impact_summary', models.TextField(default=None, max_length=10000, null=True)),
                ('possible_solution', models.TextField(max_length=10000)),
                ('contributors', models.CharField(default=None, max_length=100)),
                ('submitted_by', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('UNDER REVIEW', 'Under Review'), ('ACCEPTED', 'Accepted'), ('CLOSED/REJECTED', 'Closed/Rejected')], default='OPEN', max_length=30, null=True)),
                ('status_update', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
    ]