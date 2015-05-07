# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0016_auto_20150506_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 2, 23, 40, 784034, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 2, 23, 40, 788221, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 2, 23, 40, 786177, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
