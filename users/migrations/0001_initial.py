# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'users_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=60)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('joindate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'users', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'users_user')


    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joindate': ('django.db.models.fields.DateTimeField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['users']
