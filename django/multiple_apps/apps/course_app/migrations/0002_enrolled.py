# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_remove_user_course'),
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.Course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login_reg.User')),
            ],
        ),
    ]
