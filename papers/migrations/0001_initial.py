# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('edition', models.CharField(max_length=60)),
                ('condition', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 19, 10, 41, 86416, tzinfo=utc))),
                ('image', models.ImageField(upload_to='images')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 19, 10, 41, 87967, tzinfo=utc))),
                ('text', models.TextField(max_length=4096)),
                ('recipient', models.ForeignKey(related_name='messages_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_initiated', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 19, 10, 41, 87283, tzinfo=utc))),
                ('listing', models.ForeignKey(to='papers.Listing')),
                ('requestee', models.ForeignKey(related_name='requests_received', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(related_name='requests_sent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='request',
            field=models.ForeignKey(to='papers.Request'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='messages_sent', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
