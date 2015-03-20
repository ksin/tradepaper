# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0007_auto_20150319_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 1, 43, 11, 601681, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 1, 43, 11, 603111, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 1, 43, 11, 602476, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
