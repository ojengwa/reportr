# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150303_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='lead',
            field=models.ForeignKey(related_name='crews', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
