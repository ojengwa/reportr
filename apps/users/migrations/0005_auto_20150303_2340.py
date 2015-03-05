# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('users', '0004_auto_20150215_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parapo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rant', models.TextField()),
                ('staff', models.ForeignKey(related_name='rants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parapo',
                'verbose_name_plural': 'Parapos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80, verbose_name='name')),
                ('permissions', models.ManyToManyField(to='auth.Permission', verbose_name='permissions', blank=True)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name='email address'),
            preserve_default=True,
        ),
    ]
