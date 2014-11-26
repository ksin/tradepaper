# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.date_sent'
        db.delete_column(u'papers_message', 'date_sent')

        # Adding field 'Message.date'
        db.add_column(u'papers_message', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 25, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Message.date_sent'
        db.add_column(u'papers_message', 'date_sent',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 11, 25, 0, 0)),
                      keep_default=False)

        # Deleting field 'Message.date'
        db.delete_column(u'papers_message', 'date')


    models = {
        u'papers.listing': {
            'Meta': {'object_name': 'Listing'},
            'condition': ('django.db.models.fields.IntegerField', [], {}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 25, 0, 0)'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'papers.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages_received'", 'to': u"orm['users.User']"}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['papers.Request']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages_sent'", 'to': u"orm['users.User']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '4096'})
        },
        u'papers.request': {
            'Meta': {'object_name': 'Request'},
            'date_initiated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['papers.Listing']"}),
            'requestee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests_received'", 'to': u"orm['users.User']"}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests_sent'", 'to': u"orm['users.User']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 25, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['papers']