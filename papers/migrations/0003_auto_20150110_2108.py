# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0002_auto_20150110_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 11, 2, 8, 2, 846845, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 11, 2, 8, 2, 848345, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 11, 2, 8, 2, 847705, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
