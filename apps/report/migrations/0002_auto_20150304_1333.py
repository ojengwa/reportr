# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='report',
            name='title',
        ),
        migrations.AddField(
            model_name='report',
            name='achievements',
            field=models.TextField(default=b'loremsjhsfb jhsb jsfbjhfdbjhfbhjb '),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='challenges',
            field=models.TextField(default=b'loremsjhsfb jhsb jsfbjhfdbjhfbhjb '),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='plans',
            field=models.TextField(default=b'loremsjhsfb jhsb jsfbjhfdbjhfbhjb '),
            preserve_default=True,
        ),
    ]
