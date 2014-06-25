# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.username'
        db.delete_column(u'users_user', 'username')

        # Adding field 'User.last_login'
        db.add_column(u'users_user', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'User.name'
        db.add_column(u'users_user', 'name',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 6, 25, 0, 0), unique=True, max_length=40),
                      keep_default=False)


        # Changing field 'User.password'
        db.alter_column(u'users_user', 'password', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Adding field 'User.username'
        db.add_column(u'users_user', 'username',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=40, unique=True),
                      keep_default=False)

        # Deleting field 'User.last_login'
        db.delete_column(u'users_user', 'last_login')

        # Deleting field 'User.name'
        db.delete_column(u'users_user', 'name')


        # Changing field 'User.password'
        db.alter_column(u'users_user', 'password', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['users']