# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PredictiveFloodModelPoint'
        db.delete_table('predictive_predictivefloodmodelpoint')

        # Adding model 'PredictiveFloodNodeValue'
        db.create_table('predictive_predictivefloodnodevalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodModel'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodNode'])),
            ('elevation', self.gf('django.db.models.fields.FloatField')()),
            ('flow', self.gf('django.db.models.fields.FloatField')()),
            ('depth', self.gf('django.db.models.fields.FloatField')()),
            ('velocity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodNodeValue'])

        # Adding model 'PredictiveFloodNode'
        db.create_table('predictive_predictivefloodnode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodNode'])

        # Adding model 'Status'
        db.create_table('predictive_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['Status'])

        # Adding field 'PredictiveFloodModel.status'
        db.add_column('predictive_predictivefloodmodel', 'status',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Status'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PredictiveFloodModelPoint'
        db.create_table('predictive_predictivefloodmodelpoint', (
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodModelPoint'])

        # Deleting model 'PredictiveFloodNodeValue'
        db.delete_table('predictive_predictivefloodnodevalue')

        # Deleting model 'PredictiveFloodNode'
        db.delete_table('predictive_predictivefloodnode')

        # Deleting model 'Status'
        db.delete_table('predictive_status')

        # Deleting field 'PredictiveFloodModel.status'
        db.delete_column('predictive_predictivefloodmodel', 'status_id')


    models = {
        'predictive.annualexceedanceprobabilityscenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'AnnualExceedanceProbabilityScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.areaofsignificantpotentialrisk': {
            'Meta': {'ordering': "['name']", 'object_name': 'AreaOfSignificantPotentialRisk'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.climatescenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClimateScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.predictivefloodextent': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodExtent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveFloodModel']"})
        },
        'predictive.predictivefloodextentuncertainty': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodExtentUncertainty'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveFloodModel']"}),
            'uncertainty_band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveUncertaintyBand']"})
        },
        'predictive.predictivefloodmodel': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveFloodModel'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'aspr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AreaOfSignificantPotentialRisk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveScenario']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveSource']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Status']", 'null': 'True', 'blank': 'True'})
        },
        'predictive.predictivefloodnode': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveFloodNode'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.predictivefloodnodevalue': {
            'Meta': {'ordering': "['node']", 'object_name': 'PredictiveFloodNodeValue'},
            'depth': ('django.db.models.fields.FloatField', [], {}),
            'elevation': ('django.db.models.fields.FloatField', [], {}),
            'flow': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveFloodNode']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveFloodModel']"}),
            'velocity': ('django.db.models.fields.FloatField', [], {})
        },
        'predictive.predictivescenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'annual_exceedance_probability_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AnnualExceedanceProbabilityScenario']"}),
            'climate_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.ClimateScenario']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.predictivesource': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveSource'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.predictiveuncertaintyband': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveUncertaintyBand'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.status': {
            'Meta': {'ordering': "['name']", 'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['predictive']