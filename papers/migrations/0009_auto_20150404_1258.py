# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0008_auto_20150319_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='sent_by_requester',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 4, 17, 58, 11, 256141, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 4, 17, 58, 11, 257666, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='request',
            field=models.ForeignKey(to='papers-app.Request', related_name='messages'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='date_initiated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 4, 17, 58, 11, 257015, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
