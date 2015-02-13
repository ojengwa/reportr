# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'inquiry',
                'verbose_name_plural': 'inquiries',
            },
            bases=(models.Model,),
        ),
    ]
