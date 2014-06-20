# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.joindate'
        db.delete_column(u'users_user', 'joindate')

        # Adding unique constraint on 'User', fields ['username']
        db.create_unique(u'users_user', ['username'])

        # Adding unique constraint on 'User', fields ['email']
        db.create_unique(u'users_user', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['email']
        db.delete_unique(u'users_user', ['email'])

        # Removing unique constraint on 'User', fields ['username']
        db.delete_unique(u'users_user', ['username'])

        # Adding field 'User.joindate'
        db.add_column(u'users_user', 'joindate',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 19, 0, 0)),
                      keep_default=False)


    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['users']