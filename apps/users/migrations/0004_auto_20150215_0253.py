# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150214_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='avatar',
            new_name='picture',
        ),
    ]
