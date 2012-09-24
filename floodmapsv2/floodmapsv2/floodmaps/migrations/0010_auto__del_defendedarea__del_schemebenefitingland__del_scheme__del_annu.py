# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DefendedArea'
        db.delete_table('floodmaps_defendedarea')

        # Deleting model 'SchemeBenefitingLand'
        db.delete_table('floodmaps_schemebenefitingland')

        # Deleting model 'Scheme'
        db.delete_table('floodmaps_scheme')

        # Deleting model 'AnnualExceedanceProbabilityScenario'
        db.delete_table('floodmaps_annualexceedanceprobabilityscenario')

        # Deleting model 'SchemeChannel'
        db.delete_table('floodmaps_schemechannel')

        # Deleting model 'PredictiveFloodModel'
        db.delete_table('floodmaps_predictivefloodmodel')

        # Deleting model 'PredictiveFloodModelPoint'
        db.delete_table('floodmaps_predictivefloodmodelpoint')

        # Deleting model 'LegalInstrument'
        db.delete_table('floodmaps_legalinstrument')

        # Deleting model 'SchemeEmbankmentSection'
        db.delete_table('floodmaps_schemeembankmentsection')

        # Deleting model 'SchemeSluice'
        db.delete_table('floodmaps_schemesluice')

        # Deleting model 'ClimateScenario'
        db.delete_table('floodmaps_climatescenario')

        # Deleting model 'PredictiveFloodExtentUncertainty'
        db.delete_table('floodmaps_predictivefloodextentuncertainty')

        # Deleting model 'SchemeChannelSection'
        db.delete_table('floodmaps_schemechannelsection')

        # Deleting model 'SchemeEmbankment'
        db.delete_table('floodmaps_schemeembankment')

        # Deleting model 'IndicativeFloodDataset'
        db.delete_table('floodmaps_indicativeflooddataset')

        # Deleting model 'IndicativeFlood'
        db.delete_table('floodmaps_indicativeflood')

        # Deleting model 'IndicativeFloodCategory'
        db.delete_table('floodmaps_indicativefloodcategory')

        # Deleting model 'PredictiveScenario'
        db.delete_table('floodmaps_predictivescenario')

        # Deleting model 'PredictiveFloodExtent'
        db.delete_table('floodmaps_predictivefloodextent')

        # Deleting model 'PredictiveUncertaintyBand'
        db.delete_table('floodmaps_predictiveuncertaintyband')

        # Deleting model 'PredictiveSource'
        db.delete_table('floodmaps_predictivesource')

        # Deleting model 'SchemePumpStation'
        db.delete_table('floodmaps_schemepumpstation')

        # Deleting model 'SchemeBridge'
        db.delete_table('floodmaps_schemebridge')


    def backwards(self, orm):
        # Adding model 'DefendedArea'
        db.create_table('floodmaps_defendedarea', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('effective_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['DefendedArea'])

        # Adding model 'SchemeBenefitingLand'
        db.create_table('floodmaps_schemebenefitingland', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['SchemeBenefitingLand'])

        # Adding model 'Scheme'
        db.create_table('floodmaps_scheme', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['Scheme'])

        # Adding model 'AnnualExceedanceProbabilityScenario'
        db.create_table('floodmaps_annualexceedanceprobabilityscenario', (
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['AnnualExceedanceProbabilityScenario'])

        # Adding model 'SchemeChannel'
        db.create_table('floodmaps_schemechannel', (
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeChannel'])

        # Adding model 'PredictiveFloodModel'
        db.create_table('floodmaps_predictivefloodmodel', (
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveScenario'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveSource'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('aspr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.AreaOfSignificantPotentialRisk'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveFloodModel'])

        # Adding model 'PredictiveFloodModelPoint'
        db.create_table('floodmaps_predictivefloodmodelpoint', (
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveFloodModelPoint'])

        # Adding model 'LegalInstrument'
        db.create_table('floodmaps_legalinstrument', (
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('valid_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['LegalInstrument'])

        # Adding model 'SchemeEmbankmentSection'
        db.create_table('floodmaps_schemeembankmentsection', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeEmbankment'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeEmbankmentSection'])

        # Adding model 'SchemeSluice'
        db.create_table('floodmaps_schemesluice', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeEmbankment'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeSluice'])

        # Adding model 'ClimateScenario'
        db.create_table('floodmaps_climatescenario', (
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['ClimateScenario'])

        # Adding model 'PredictiveFloodExtentUncertainty'
        db.create_table('floodmaps_predictivefloodextentuncertainty', (
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('uncertainty_band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveUncertaintyBand'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveFloodExtentUncertainty'])

        # Adding model 'SchemeChannelSection'
        db.create_table('floodmaps_schemechannelsection', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeChannel'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeChannelSection'])

        # Adding model 'SchemeEmbankment'
        db.create_table('floodmaps_schemeembankment', (
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeEmbankment'])

        # Adding model 'IndicativeFloodDataset'
        db.create_table('floodmaps_indicativeflooddataset', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metadata', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['IndicativeFloodDataset'])

        # Adding model 'IndicativeFlood'
        db.create_table('floodmaps_indicativeflood', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.IndicativeFloodCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.IndicativeFloodDataset'])),
        ))
        db.send_create_signal('floodmaps', ['IndicativeFlood'])

        # Adding model 'IndicativeFloodCategory'
        db.create_table('floodmaps_indicativefloodcategory', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['IndicativeFloodCategory'])

        # Adding model 'PredictiveScenario'
        db.create_table('floodmaps_predictivescenario', (
            ('annual_exceedance_probability_scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.AnnualExceedanceProbabilityScenario'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('climate_scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.ClimateScenario'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveScenario'])

        # Adding model 'PredictiveFloodExtent'
        db.create_table('floodmaps_predictivefloodextent', (
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.PredictiveFloodModel'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PolygonField')(srid=2157)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveFloodExtent'])

        # Adding model 'PredictiveUncertaintyBand'
        db.create_table('floodmaps_predictiveuncertaintyband', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveUncertaintyBand'])

        # Adding model 'PredictiveSource'
        db.create_table('floodmaps_predictivesource', (
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('floodmaps', ['PredictiveSource'])

        # Adding model 'SchemePumpStation'
        db.create_table('floodmaps_schemepumpstation', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemePumpStation'])

        # Adding model 'SchemeBridge'
        db.create_table('floodmaps_schemebridge', (
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeChannel'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeBridge'])


    models = {
        'floodmaps.approvalstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'ApprovalStatus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'floodmaps.areaofsignificantpotentialrisk': {
            'Meta': {'ordering': "['name']", 'object_name': 'AreaOfSignificantPotentialRisk'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.datasource': {
            'Meta': {'ordering': "['name']", 'object_name': 'DataSource'},
            'default_folder': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodaddress': {
            'Meta': {'ordering': "['flood']", 'object_name': 'FloodAddress'},
            'building_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.County']", 'null': 'True', 'blank': 'True'}),
            'easting': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'grid_reference': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'northing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']", 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Town']", 'null': 'True', 'blank': 'True'}),
            'townland': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Townland']", 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.floodcause': {
            'Meta': {'ordering': "['name']", 'object_name': 'FloodCause'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodcauselink': {
            'Meta': {'object_name': 'FloodCauseLink'},
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodCause']"}),
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']", 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.floodgroup': {
            'Meta': {'ordering': "['type']", 'object_name': 'FloodGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodGroupType']"})
        },
        'floodmaps.floodgrouptype': {
            'Meta': {'ordering': "['name']", 'object_name': 'FloodGroupType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodrecordtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'FloodRecordType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodreportlink': {
            'Meta': {'object_name': 'FloodReportLink'},
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']", 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.floodsourcetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'FloodSourceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.geographicalquality': {
            'Meta': {'ordering': "['name']", 'object_name': 'GeographicalQuality'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.glossary': {
            'Meta': {'ordering': "['category', 'term']", 'object_name': 'Glossary'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.GlossaryCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'floodmaps.glossarycategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'GlossaryCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.historicflood': {
            'Meta': {'ordering': "['name']", 'object_name': 'HistoricFlood'},
            'alleviation_scheme': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'catchment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Catchment']", 'null': 'True', 'blank': 'True'}),
            'cause': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.FloodCause']", 'through': "orm['floodmaps.FloodCauseLink']", 'symmetrical': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'flood_record_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodRecordType']", 'null': 'True', 'blank': 'True'}),
            'geographical_quality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.GeographicalQuality']", 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['floodmaps.FloodGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapping_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mapping_checked_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'peak_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.Report']", 'symmetrical': 'False'}),
            'scheme_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'severity_index': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'source_coastal_water': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.CoastalWater']", 'null': 'True', 'blank': 'True'}),
            'source_lake': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Lake']", 'null': 'True', 'blank': 'True'}),
            'source_other': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'source_river': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.River']", 'null': 'True', 'blank': 'True'}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodSourceType']", 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.historicfloodinterpretation': {
            'Meta': {'ordering': "['flood']", 'object_name': 'HistoricFloodInterpretation'},
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justification': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quality_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.QualityCode']"}),
            'stage_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.interpretationstage': {
            'Meta': {'ordering': "['name']", 'object_name': 'InterpretationStage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'floodmaps.qualitycode': {
            'Meta': {'ordering': "['name']", 'object_name': 'QualityCode'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'floodmaps.report': {
            'Meta': {'object_name': 'Report'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {}),
            'report_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.ReportType']", 'null': 'True'})
        },
        'floodmaps.reportaddress': {
            'Meta': {'ordering': "['report']", 'object_name': 'ReportAddress'},
            'building_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.County']", 'null': 'True', 'blank': 'True'}),
            'easting': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grid_reference': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'northing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Town']", 'null': 'True', 'blank': 'True'}),
            'townland': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Townland']", 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.reportinterpretation': {
            'Meta': {'ordering': "['report']", 'object_name': 'ReportInterpretation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interpretation_stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.InterpretationStage']"}),
            'justification': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quality_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.QualityCode']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']"}),
            'stage_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.reporttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ReportType'},
            'default_extension': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'default_folder': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'geography.catchment': {
            'Meta': {'ordering': "['name', 'hydrometric_area']", 'object_name': 'Catchment'},
            'area_sq_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'hydrometric_area': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'perimiter_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'geography.coastalwater': {
            'Meta': {'ordering': "['name']", 'object_name': 'CoastalWater'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'geography.county': {
            'Meta': {'ordering': "['name']", 'object_name': 'County'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irish_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'geography.districtelectoraldivision': {
            'Meta': {'ordering': "['name']", 'object_name': 'DistrictElectoralDivision'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.County']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'geography.lake': {
            'Meta': {'ordering': "['name', 'hydrometric_area']", 'object_name': 'Lake'},
            'area_sq_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'hydrometric_area': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'perimiter_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'seg_cd': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'geography.river': {
            'Meta': {'ordering': "['name']", 'object_name': 'River'},
            'catchment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Catchment']"}),
            'down_stream_length': ('django.db.models.fields.FloatField', [], {}),
            'epa_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'flow_direction': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'up_stream_length': ('django.db.models.fields.FloatField', [], {})
        },
        'geography.town': {
            'Meta': {'ordering': "['name']", 'object_name': 'Town'},
            'centroid_x': ('django.db.models.fields.FloatField', [], {}),
            'centroid_y': ('django.db.models.fields.FloatField', [], {}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.County']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irish_class': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'irish_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_and_county': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'town_category': ('django.db.models.fields.IntegerField', [], {})
        },
        'geography.townland': {
            'Meta': {'ordering': "['name']", 'object_name': 'Townland'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.County']"}),
            'ded': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.DistrictElectoralDivision']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'os_townland_id': ('django.db.models.fields.IntegerField', [], {}),
            'upper': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['floodmaps']