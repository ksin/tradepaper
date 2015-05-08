# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0021_auto_20150508_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 27, 54, 320925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 27, 54, 323714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 22, 27, 54, 322682, tzinfo=utc)),
        ),
    ]
