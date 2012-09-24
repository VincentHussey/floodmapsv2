# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AreaOfSignificantPotentialRisk'
        db.create_table('predictive_areaofsignificantpotentialrisk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['AreaOfSignificantPotentialRisk'])

        # Adding model 'ClimateScenario'
        db.create_table('predictive_climatescenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['ClimateScenario'])

        # Adding model 'AnnualExceedanceProbabilityScenario'
        db.create_table('predictive_annualexceedanceprobabilityscenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['AnnualExceedanceProbabilityScenario'])

        # Adding model 'PredictiveSource'
        db.create_table('predictive_predictivesource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['PredictiveSource'])

        # Adding model 'PredictiveScenario'
        db.create_table('predictive_predictivescenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('climate_scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.ClimateScenario'])),
            ('annual_exceedance_probability_scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.AnnualExceedanceProbabilityScenario'])),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['PredictiveScenario'])

        # Adding model 'PredictiveUncertaintyBand'
        db.create_table('predictive_predictiveuncertaintyband', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['PredictiveUncertaintyBand'])

        # Adding model 'PredictiveFloodModel'
        db.create_table('predictive_predictivefloodmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveScenario'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveSource'])),
            ('aspr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.AreaOfSignificantPotentialRisk'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodModel'])

        # Adding model 'PredictiveFloodModelPoint'
        db.create_table('predictive_predictivefloodmodelpoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodModelPoint'])

        # Adding model 'PredictiveFloodExtent'
        db.create_table('predictive_predictivefloodextent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PolygonField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodExtent'])

        # Adding model 'PredictiveFloodExtentUncertainty'
        db.create_table('predictive_predictivefloodextentuncertainty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveFloodModel'])),
            ('uncertainty_band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.PredictiveUncertaintyBand'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['PredictiveFloodExtentUncertainty'])


    def backwards(self, orm):
        # Deleting model 'AreaOfSignificantPotentialRisk'
        db.delete_table('predictive_areaofsignificantpotentialrisk')

        # Deleting model 'ClimateScenario'
        db.delete_table('predictive_climatescenario')

        # Deleting model 'AnnualExceedanceProbabilityScenario'
        db.delete_table('predictive_annualexceedanceprobabilityscenario')

        # Deleting model 'PredictiveSource'
        db.delete_table('predictive_predictivesource')

        # Deleting model 'PredictiveScenario'
        db.delete_table('predictive_predictivescenario')

        # Deleting model 'PredictiveUncertaintyBand'
        db.delete_table('predictive_predictiveuncertaintyband')

        # Deleting model 'PredictiveFloodModel'
        db.delete_table('predictive_predictivefloodmodel')

        # Deleting model 'PredictiveFloodModelPoint'
        db.delete_table('predictive_predictivefloodmodelpoint')

        # Deleting model 'PredictiveFloodExtent'
        db.delete_table('predictive_predictivefloodextent')

        # Deleting model 'PredictiveFloodExtentUncertainty'
        db.delete_table('predictive_predictivefloodextentuncertainty')


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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveSource']"})
        },
        'predictive.predictivefloodmodelpoint': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodModelPoint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.PredictiveFloodModel']"})
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
        }
    }

    complete_apps = ['predictive']