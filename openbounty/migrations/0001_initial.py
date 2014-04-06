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
            ('bounty', self.gf('django.db.models.fields.DecimalField')(max_digits=500, decimal_places=2)),
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
            ('wallet', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=500, decimal_places=2)),
            ('access_token', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('venmo', self.gf('django.db.models.fields.CharField')(default='', max_length=60, blank=True)),
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

        # Adding model 'Proof'
        db.create_table(u'openbounty_proof', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
            ('challenge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.Challenge'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('winner', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'openbounty', ['Proof'])

        # Adding model 'ClaimVotes'
        db.create_table(u'openbounty_claimvotes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.BountyUser'])),
            ('claim', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['openbounty.Proof'])),
        ))
        db.send_create_signal(u'openbounty', ['ClaimVotes'])


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

        # Deleting model 'Proof'
        db.delete_table(u'openbounty_proof')

        # Deleting model 'ClaimVotes'
        db.delete_table(u'openbounty_claimvotes')


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
            'access_token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'venmo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'wallet': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '500', 'decimal_places': '2'})
        },
        u'openbounty.challenge': {
            'Meta': {'object_name': 'Challenge'},
            'backers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'backings'", 'symmetrical': 'False', 'through': u"orm['openbounty.Backing']", 'to': u"orm['openbounty.BountyUser']"}),
            'bounty': ('django.db.models.fields.DecimalField', [], {'max_digits': '500', 'decimal_places': '2'}),
            'challenge': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'doers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'proofs'", 'symmetrical': 'False', 'through': u"orm['openbounty.Proof']", 'to': u"orm['openbounty.BountyUser']"}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        },
        u'openbounty.claimvotes': {
            'Meta': {'object_name': 'ClaimVotes'},
            'claim': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.Proof']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"})
        },
        u'openbounty.proof': {
            'Meta': {'object_name': 'Proof'},
            'challenge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.Challenge']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['openbounty.BountyUser']"}),
            'voters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'claim_votes'", 'symmetrical': 'False', 'through': u"orm['openbounty.ClaimVotes']", 'to': u"orm['openbounty.BountyUser']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['openbounty']