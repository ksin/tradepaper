# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150112_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 4, 33, 7, 3148, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
