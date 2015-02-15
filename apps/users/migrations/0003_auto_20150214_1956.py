# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150214_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
    ]
