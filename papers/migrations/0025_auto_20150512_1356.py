# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers-app', '0024_auto_20150512_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='edition',
            new_name='issue',
        ),
    ]
