# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('edition', models.CharField(max_length=60)),
                ('condition', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 9, 55, 0, 528934, tzinfo=utc))),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 9, 55, 0, 530936, tzinfo=utc))),
                ('text', models.TextField(max_length=4096)),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='messages_received')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_initiated', models.DateTimeField(default=datetime.datetime(2015, 1, 10, 9, 55, 0, 530042, tzinfo=utc))),
                ('listing', models.ForeignKey(to='papers.Listing')),
                ('requestee', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='requests_received')),
                ('requester', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='requests_sent')),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='messages_sent'),
            preserve_default=True,
        ),
    ]
