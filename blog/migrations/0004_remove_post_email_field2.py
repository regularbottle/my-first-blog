# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_email_field2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email_field2',
        ),
    ]
