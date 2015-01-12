# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0004_auto_20150112_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 6, 58, 54, 276037, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 6, 58, 54, 277570, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 6, 58, 54, 276899, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
