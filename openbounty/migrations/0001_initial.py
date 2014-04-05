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
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('fulfilled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
        ))
        db.send_create_signal(u'openbounty', ['Challenge'])

        # Adding model 'BountyUser'
        db.create_table(u'openbounty_bountyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'openbounty', ['BountyUser'])

        # Adding M2M table for field groups on 'BountyUser'
        m2m_table_name = db.shorten_name(u'openbounty_bountyuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bountyuser', models.ForeignKey(orm[u'openbounty.bountyuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bountyuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'BountyUser'
        m2m_table_name = db.shorten_name(u'openbounty_bountyuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bountyuser', models.ForeignKey(orm[u'openbounty.bountyuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bountyuser_id', 'permission_id'])

        # Adding model 'Backing'
        db.create_table(u'openbounty_backing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
            ('challenge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.Challenge'])),
        ))
        db.send_create_signal(u'openbounty', ['Backing'])

        # Adding model 'Comment'
        db.create_table(u'openbounty_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
            ('challenge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.Challenge'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'openbounty', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Challenge'
        db.delete_table(u'openbounty_challenge')

        # Deleting model 'BountyUser'
        db.delete_table(u'openbounty_bountyuser')

        # Removing M2M table for field groups on 'BountyUser'
        db.delete_table(db.shorten_name(u'openbounty_bountyuser_groups'))

        # Removing M2M table for field user_permissions on 'BountyUser'
        db.delete_table(db.shorten_name(u'openbounty_bountyuser_user_permissions'))

        # Deleting model 'Backing'
        db.delete_table(u'openbounty_backing')

        # Deleting model 'Comment'
        db.delete_table(u'openbounty_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'openbounty.backing': {
            'Meta': {'object_name': 'Backing'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.Challenge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        },
        u'openbounty.bountyuser': {
            'Meta': {'object_name': 'BountyUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'openbounty.challenge': {
            'Meta': {'object_name': 'Challenge'},
            'backers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'backings'", 'symmetrical': 'False', 'through': u"orm['openbounty.Backing']", 'to': u"orm['openbounty.BountyUser']"}),
            'bounty': ('django.db.models.fields.FloatField', [], {}),
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        },
        u'openbounty.comment': {
            'Meta': {'object_name': 'Comment'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.Challenge']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        }
    }

    complete_apps = ['openbounty']