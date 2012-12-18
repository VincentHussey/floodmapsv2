# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SchemePumpStation'
        db.delete_table('works_schemepumpstation')

        # Deleting model 'SchemeSluice'
        db.delete_table('works_schemesluice')

        # Deleting model 'SchemeBenefitingLand'
        db.delete_table('works_schemebenefitingland')

        # Deleting model 'SchemeEmbankment'
        db.delete_table('works_schemeembankment')

        # Deleting model 'SchemeBridge'
        db.delete_table('works_schemebridge')

        # Deleting model 'SchemeChannelSection'
        db.delete_table('works_schemechannelsection')

        # Deleting model 'SchemeEmbankmentSection'
        db.delete_table('works_schemeembankmentsection')

        # Deleting model 'SchemeChannel'
        db.delete_table('works_schemechannel')

        # Adding model 'Embankment'
        db.create_table('works_embankment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('works', ['Embankment'])

        # Adding model 'ChannelSection'
        db.create_table('works_channelsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Channel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('works', ['ChannelSection'])

        # Adding model 'Sluice'
        db.create_table('works_sluice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Embankment'])),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['Sluice'])

        # Adding model 'BenefitingLand'
        db.create_table('works_benefitingland', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('drained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('works', ['BenefitingLand'])

        # Adding model 'EmbankmentSection'
        db.create_table('works_embankmentsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Embankment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('works', ['EmbankmentSection'])

        # Adding model 'PumpStation'
        db.create_table('works_pumpstation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['PumpStation'])

        # Adding model 'Channel'
        db.create_table('works_channel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('works', ['Channel'])

        # Adding model 'Bridge'
        db.create_table('works_bridge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Channel'])),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['Bridge'])


    def backwards(self, orm):
        # Adding model 'SchemePumpStation'
        db.create_table('works_schemepumpstation', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemePumpStation'])

        # Adding model 'SchemeSluice'
        db.create_table('works_schemesluice', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeEmbankment'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeSluice'])

        # Adding model 'SchemeBenefitingLand'
        db.create_table('works_schemebenefitingland', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('works', ['SchemeBenefitingLand'])

        # Adding model 'SchemeEmbankment'
        db.create_table('works_schemeembankment', (
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeEmbankment'])

        # Adding model 'SchemeBridge'
        db.create_table('works_schemebridge', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeChannel'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeBridge'])

        # Adding model 'SchemeChannelSection'
        db.create_table('works_schemechannelsection', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeChannel'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeChannelSection'])

        # Adding model 'SchemeEmbankmentSection'
        db.create_table('works_schemeembankmentsection', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeEmbankment'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeEmbankmentSection'])

        # Adding model 'SchemeChannel'
        db.create_table('works_schemechannel', (
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeChannel'])

        # Deleting model 'Embankment'
        db.delete_table('works_embankment')

        # Deleting model 'ChannelSection'
        db.delete_table('works_channelsection')

        # Deleting model 'Sluice'
        db.delete_table('works_sluice')

        # Deleting model 'BenefitingLand'
        db.delete_table('works_benefitingland')

        # Deleting model 'EmbankmentSection'
        db.delete_table('works_embankmentsection')

        # Deleting model 'PumpStation'
        db.delete_table('works_pumpstation')

        # Deleting model 'Channel'
        db.delete_table('works_channel')

        # Deleting model 'Bridge'
        db.delete_table('works_bridge')


    models = {
        'works.benefitingland': {
            'Meta': {'ordering': "['scheme']", 'object_name': 'BenefitingLand'},
            'drained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.bridge': {
            'Meta': {'ordering': "['channel', 'ref']", 'object_name': 'Bridge'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Channel']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.channel': {
            'Meta': {'ordering': "['scheme', 'ref']", 'object_name': 'Channel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.channelsection': {
            'Meta': {'ordering': "['channel', 'name']", 'object_name': 'ChannelSection'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Channel']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.defendedarea': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'DefendedArea'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'effective_from': ('django.db.models.fields.DateTimeField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.embankment': {
            'Meta': {'ordering': "['scheme', 'ref']", 'object_name': 'Embankment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.embankmentsection': {
            'Meta': {'ordering': "['embankment', 'name']", 'object_name': 'EmbankmentSection'},
            'embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Embankment']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.legalinstrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'LegalInstrument'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'works.pumpstation': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'PumpStation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.scheme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scheme'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.sluice': {
            'Meta': {'ordering': "['embankment', 'ref']", 'object_name': 'Sluice'},
            'embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Embankment']"}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['works']