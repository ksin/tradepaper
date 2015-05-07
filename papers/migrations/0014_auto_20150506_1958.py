# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('papers-app', '0013_auto_20150408_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_initiated', models.DateTimeField(default=datetime.datetime(2015, 5, 7, 0, 58, 29, 673514, tzinfo=utc))),
                ('listing', models.ForeignKey(to='papers-app.Listing')),
                ('tradee', models.ForeignKey(related_name='trades_received', to=settings.AUTH_USER_MODEL)),
                ('trader', models.ForeignKey(related_name='trades_sent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='request',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='request',
            name='requestee',
        ),
        migrations.RemoveField(
            model_name='request',
            name='requester',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sent_by_requester',
            new_name='sent_by_trader',
        ),
        migrations.RemoveField(
            model_name='message',
            name='request',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.AddField(
            model_name='message',
            name='trade',
            field=models.ForeignKey(related_name='messages', null=True, to='papers-app.Trade'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 0, 58, 29, 672712, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 0, 58, 29, 674105, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
