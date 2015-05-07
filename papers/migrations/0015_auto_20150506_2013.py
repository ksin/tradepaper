# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0014_auto_20150506_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 1, 13, 36, 54457, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 1, 13, 36, 55852, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 1, 13, 36, 55261, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
