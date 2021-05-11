# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-27 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0004_auto_20191113_0334'),
        ('academic_procedures', '0010_auto_20191127_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2019)),
                ('semester', models.IntegerField()),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.Student')),
            ],
            options={
                'db_table': 'Register',
            },
        ),
        migrations.AlterUniqueTogether(
            name='register',
            unique_together=set([('curr_id', 'student_id')]),
        ),
    ]
