# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0010_auto_20150404_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 0, 57, 28, 480552, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 0, 57, 28, 481991, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='request',
            field=models.ForeignKey(null=True, to='papers-app.Request', related_name='messages'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 0, 57, 28, 481406, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
