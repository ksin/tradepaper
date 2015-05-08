# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0018_auto_20150506_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 21, 50, 51, 219874, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(editable=False, max_length=22, blank=True, serialize=False, unique=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 21, 50, 51, 222756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(editable=False, max_length=22, blank=True, serialize=False, unique=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 21, 50, 51, 221326, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trade',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(editable=False, max_length=22, blank=True, serialize=False, unique=True, primary_key=True),
        ),
    ]
