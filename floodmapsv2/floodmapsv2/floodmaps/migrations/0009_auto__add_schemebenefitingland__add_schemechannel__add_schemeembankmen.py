# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SchemeBenefitingLand'
        db.create_table('floodmaps_schemebenefitingland', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemeBenefitingLand'])

        # Adding model 'SchemeChannel'
        db.create_table('floodmaps_schemechannel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeChannel'])

        # Adding model 'SchemeEmbankmentSection'
        db.create_table('floodmaps_schemeembankmentsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeEmbankment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemeEmbankmentSection'])

        # Adding model 'SchemeSluice'
        db.create_table('floodmaps_schemesluice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_embankment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeEmbankment'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemeSluice'])

        # Adding model 'SchemeChannelSection'
        db.create_table('floodmaps_schemechannelsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeChannel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemeChannelSection'])

        # Adding model 'SchemeEmbankment'
        db.create_table('floodmaps_schemeembankment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['SchemeEmbankment'])

        # Adding model 'SchemeBridge'
        db.create_table('floodmaps_schemebridge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.SchemeChannel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemeBridge'])

        # Adding model 'SchemePumpStation'
        db.create_table('floodmaps_schemepumpstation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Scheme'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('floodmaps', ['SchemePumpStation'])


        # Changing field 'DefendedArea.geometry'
        db.alter_column('floodmaps_defendedarea', 'geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157))

    def backwards(self, orm):
        # Deleting model 'SchemeBenefitingLand'
        db.delete_table('floodmaps_schemebenefitingland')

        # Deleting model 'SchemeChannel'
        db.delete_table('floodmaps_schemechannel')

        # Deleting model 'SchemeEmbankmentSection'
        db.delete_table('floodmaps_schemeembankmentsection')

        # Deleting model 'SchemeSluice'
        db.delete_table('floodmaps_schemesluice')

        # Deleting model 'SchemeChannelSection'
        db.delete_table('floodmaps_schemechannelsection')

        # Deleting model 'SchemeEmbankment'
        db.delete_table('floodmaps_schemeembankment')

        # Deleting model 'SchemeBridge'
        db.delete_table('floodmaps_schemebridge')

        # Deleting model 'SchemePumpStation'
        db.delete_table('floodmaps_schemepumpstation')


        # Changing field 'DefendedArea.geometry'
        db.alter_column('floodmaps_defendedarea', 'geometry', self.gf('django.contrib.gis.db.models.fields.PolygonField')(srid=2157))

    models = {
        'floodmaps.annualexceedanceprobabilityscenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'AnnualExceedanceProbabilityScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
        'floodmaps.climatescenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClimateScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'floodmaps.defendedarea': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'DefendedArea'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'effective_from': ('django.db.models.fields.DateTimeField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Scheme']"})
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
        'floodmaps.indicativeflood': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFlood'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.IndicativeFloodCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.IndicativeFloodDataset']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.indicativefloodcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFloodCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.indicativeflooddataset': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFloodDataset'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.interpretationstage': {
            'Meta': {'ordering': "['name']", 'object_name': 'InterpretationStage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'floodmaps.legalinstrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'LegalInstrument'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'floodmaps.predictivefloodextent': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodExtent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveFloodModel']"})
        },
        'floodmaps.predictivefloodextentuncertainty': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodExtentUncertainty'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveFloodModel']"}),
            'uncertainty_band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveUncertaintyBand']"})
        },
        'floodmaps.predictivefloodmodel': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveFloodModel'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'aspr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.AreaOfSignificantPotentialRisk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveScenario']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveSource']"})
        },
        'floodmaps.predictivefloodmodelpoint': {
            'Meta': {'ordering': "['parent']", 'object_name': 'PredictiveFloodModelPoint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.PredictiveFloodModel']"})
        },
        'floodmaps.predictivescenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveScenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'annual_exceedance_probability_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.AnnualExceedanceProbabilityScenario']"}),
            'climate_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.ClimateScenario']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.predictivesource': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveSource'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.predictiveuncertaintyband': {
            'Meta': {'ordering': "['name']", 'object_name': 'PredictiveUncertaintyBand'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'floodmaps.scheme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scheme'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.schemebenefitingland': {
            'Meta': {'ordering': "['scheme']", 'object_name': 'SchemeBenefitingLand'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Scheme']"})
        },
        'floodmaps.schemebridge': {
            'Meta': {'ordering': "['scheme_channel', 'name']", 'object_name': 'SchemeBridge'},
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.SchemeChannel']"})
        },
        'floodmaps.schemechannel': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemeChannel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Scheme']"})
        },
        'floodmaps.schemechannelsection': {
            'Meta': {'ordering': "['scheme_channel', 'name']", 'object_name': 'SchemeChannelSection'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.SchemeChannel']"})
        },
        'floodmaps.schemeembankment': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemeEmbankment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Scheme']"})
        },
        'floodmaps.schemeembankmentsection': {
            'Meta': {'ordering': "['scheme_embankment', 'name']", 'object_name': 'SchemeEmbankmentSection'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.SchemeEmbankment']"})
        },
        'floodmaps.schemepumpstation': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'SchemePumpStation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Scheme']"})
        },
        'floodmaps.schemesluice': {
            'Meta': {'ordering': "['scheme_embankment', 'name']", 'object_name': 'SchemeSluice'},
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme_embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.SchemeEmbankment']"})
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