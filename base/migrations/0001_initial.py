# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('dni', models.CharField(unique=True, max_length=9)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(unique=True, max_length=75, blank=True)),
                ('category', models.CharField(max_length=11, choices=[(b'B', b'Beneficiary'), (b'E', b'Employee'), (b'V', b'Volunteer')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
