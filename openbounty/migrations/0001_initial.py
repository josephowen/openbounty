# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Challenge'
        db.create_table(u'openbounty_challenge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bounty', self.gf('django.db.models.fields.FloatField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('challenge', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
        ))
        db.send_create_signal(u'openbounty', ['Challenge'])

        # Adding model 'BountyUser'
        db.create_table(u'openbounty_bountyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40, db_index=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'openbounty', ['BountyUser'])


    def backwards(self, orm):
        # Deleting model 'Challenge'
        db.delete_table(u'openbounty_challenge')

        # Deleting model 'BountyUser'
        db.delete_table(u'openbounty_bountyuser')


    models = {
        u'openbounty.bountyuser': {
            'Meta': {'object_name': 'BountyUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'openbounty.challenge': {
            'Meta': {'object_name': 'Challenge'},
            'bounty': ('django.db.models.fields.FloatField', [], {}),
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        }
    }

    complete_apps = ['openbounty']