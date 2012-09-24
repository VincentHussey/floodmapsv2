# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LegalInstrument'
        db.create_table('works_legalinstrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('valid_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('works', ['LegalInstrument'])

        # Adding model 'Scheme'
        db.create_table('works_scheme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('works', ['Scheme'])

        # Adding model 'DefendedArea'
        db.create_table('works_defendedarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('effective_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('works', ['DefendedArea'])

        # Adding model 'SchemeChannel'
        db.create_table('works_schemechannel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeChannel'])

        # Adding model 'SchemeChannelSection'
        db.create_table('works_schemechannelsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeChannel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemeChannelSection'])

        # Adding model 'SchemeEmbankment'
        db.create_table('works_schemeembankment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('works', ['SchemeEmbankment'])

        # Adding model 'SchemeEmbankmentSection'
        db.create_table('works_schemeembankmentsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeEmbankment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemeEmbankmentSection'])

        # Adding model 'SchemeBenefitingLand'
        db.create_table('works_schemebenefitingland', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemeBenefitingLand'])

        # Adding model 'SchemeBridge'
        db.create_table('works_schemebridge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeChannel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemeBridge'])

        # Adding model 'SchemeSluice'
        db.create_table('works_schemesluice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.SchemeEmbankment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemeSluice'])

        # Adding model 'SchemePumpStation'
        db.create_table('works_schemepumpstation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['works.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('works', ['SchemePumpStation'])


    def backwards(self, orm):
        # Deleting model 'LegalInstrument'
        db.delete_table('works_legalinstrument')

        # Deleting model 'Scheme'
        db.delete_table('works_scheme')

        # Deleting model 'DefendedArea'
        db.delete_table('works_defendedarea')

        # Deleting model 'SchemeChannel'
        db.delete_table('works_schemechannel')

        # Deleting model 'SchemeChannelSection'
        db.delete_table('works_schemechannelsection')

        # Deleting model 'SchemeEmbankment'
        db.delete_table('works_schemeembankment')

        # Deleting model 'SchemeEmbankmentSection'
        db.delete_table('works_schemeembankmentsection')

        # Deleting model 'SchemeBenefitingLand'
        db.delete_table('works_schemebenefitingland')

        # Deleting model 'SchemeBridge'
        db.delete_table('works_schemebridge')

        # Deleting model 'SchemeSluice'
        db.delete_table('works_schemesluice')

        # Deleting model 'SchemePumpStation'
        db.delete_table('works_schemepumpstation')


    models = {
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
        'works.legalinstrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'LegalInstrument'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'works.scheme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scheme'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.schemebenefitingland': {
            'Meta': {'ordering': "['scheme']", 'object_name': 'SchemeBenefitingLand'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.schemebridge': {
            'Meta': {'ordering': "['scheme_channel', 'name']", 'object_name': 'SchemeBridge'},
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.SchemeChannel']"})
        },
        'works.schemechannel': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemeChannel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.schemechannelsection': {
            'Meta': {'ordering': "['scheme_channel', 'name']", 'object_name': 'SchemeChannelSection'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.SchemeChannel']"})
        },
        'works.schemeembankment': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemeEmbankment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.schemeembankmentsection': {
            'Meta': {'ordering': "['scheme_embankment', 'name']", 'object_name': 'SchemeEmbankmentSection'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.SchemeEmbankment']"})
        },
        'works.schemepumpstation': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemePumpStation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.schemesluice': {
            'Meta': {'ordering': "['scheme_embankment', 'name']", 'object_name': 'SchemeSluice'},
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.SchemeEmbankment']"})
        }
    }

    complete_apps = ['works']