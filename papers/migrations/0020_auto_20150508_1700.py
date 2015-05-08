# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0019_auto_20150508_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 0, 35, 932826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 0, 35, 935465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 0, 35, 934453, tzinfo=utc)),
        ),
    ]
