# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeographicalQuality'
        db.create_table('floodmaps_geographicalquality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['GeographicalQuality'])

        # Adding field 'ReportAddress.townland'
        db.add_column('floodmaps_reportaddress', 'townland',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Townland'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.town'
        db.add_column('floodmaps_reportaddress', 'town',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Town'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.county'
        db.add_column('floodmaps_reportaddress', 'county',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.County'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.name'
        db.add_column('floodmaps_reportaddress', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.building_number'
        db.add_column('floodmaps_reportaddress', 'building_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.street'
        db.add_column('floodmaps_reportaddress', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.easting'
        db.add_column('floodmaps_reportaddress', 'easting',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.northing'
        db.add_column('floodmaps_reportaddress', 'northing',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReportAddress.grid_reference'
        db.add_column('floodmaps_reportaddress', 'grid_reference',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.style'
        db.add_column('floodmaps_historicflood', 'style',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.source_type'
        db.add_column('floodmaps_historicflood', 'source_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.FloodSourceType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.source_river'
        db.add_column('floodmaps_historicflood', 'source_river',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.River'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.source_lake'
        db.add_column('floodmaps_historicflood', 'source_lake',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Lake'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.source_coastal_water'
        db.add_column('floodmaps_historicflood', 'source_coastal_water',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.CoastalWater'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.source_other'
        db.add_column('floodmaps_historicflood', 'source_other',
                      self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.catchment'
        db.add_column('floodmaps_historicflood', 'catchment',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Catchment'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.peak_datetime'
        db.add_column('floodmaps_historicflood', 'peak_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.alleviation_scheme'
        db.add_column('floodmaps_historicflood', 'alleviation_scheme',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HistoricFlood.scheme_description'
        db.add_column('floodmaps_historicflood', 'scheme_description',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.severity_index'
        db.add_column('floodmaps_historicflood', 'severity_index',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'HistoricFlood.geographical_quality'
        db.add_column('floodmaps_historicflood', 'geographical_quality',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.GeographicalQuality'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HistoricFlood.mapping_checked'
        db.add_column('floodmaps_historicflood', 'mapping_checked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HistoricFlood.mapping_checked_date'
        db.add_column('floodmaps_historicflood', 'mapping_checked_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.townland'
        db.add_column('floodmaps_floodaddress', 'townland',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Townland'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.town'
        db.add_column('floodmaps_floodaddress', 'town',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Town'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.county'
        db.add_column('floodmaps_floodaddress', 'county',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.County'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.name'
        db.add_column('floodmaps_floodaddress', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.building_number'
        db.add_column('floodmaps_floodaddress', 'building_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.street'
        db.add_column('floodmaps_floodaddress', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.easting'
        db.add_column('floodmaps_floodaddress', 'easting',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.northing'
        db.add_column('floodmaps_floodaddress', 'northing',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FloodAddress.grid_reference'
        db.add_column('floodmaps_floodaddress', 'grid_reference',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'GeographicalQuality'
        db.delete_table('floodmaps_geographicalquality')

        # Deleting field 'ReportAddress.townland'
        db.delete_column('floodmaps_reportaddress', 'townland_id')

        # Deleting field 'ReportAddress.town'
        db.delete_column('floodmaps_reportaddress', 'town_id')

        # Deleting field 'ReportAddress.county'
        db.delete_column('floodmaps_reportaddress', 'county_id')

        # Deleting field 'ReportAddress.name'
        db.delete_column('floodmaps_reportaddress', 'name')

        # Deleting field 'ReportAddress.building_number'
        db.delete_column('floodmaps_reportaddress', 'building_number')

        # Deleting field 'ReportAddress.street'
        db.delete_column('floodmaps_reportaddress', 'street')

        # Deleting field 'ReportAddress.easting'
        db.delete_column('floodmaps_reportaddress', 'easting')

        # Deleting field 'ReportAddress.northing'
        db.delete_column('floodmaps_reportaddress', 'northing')

        # Deleting field 'ReportAddress.grid_reference'
        db.delete_column('floodmaps_reportaddress', 'grid_reference')

        # Deleting field 'HistoricFlood.style'
        db.delete_column('floodmaps_historicflood', 'style')

        # Deleting field 'HistoricFlood.source_type'
        db.delete_column('floodmaps_historicflood', 'source_type_id')

        # Deleting field 'HistoricFlood.source_river'
        db.delete_column('floodmaps_historicflood', 'source_river_id')

        # Deleting field 'HistoricFlood.source_lake'
        db.delete_column('floodmaps_historicflood', 'source_lake_id')

        # Deleting field 'HistoricFlood.source_coastal_water'
        db.delete_column('floodmaps_historicflood', 'source_coastal_water_id')

        # Deleting field 'HistoricFlood.source_other'
        db.delete_column('floodmaps_historicflood', 'source_other')

        # Deleting field 'HistoricFlood.catchment'
        db.delete_column('floodmaps_historicflood', 'catchment_id')

        # Deleting field 'HistoricFlood.peak_datetime'
        db.delete_column('floodmaps_historicflood', 'peak_datetime')

        # Deleting field 'HistoricFlood.alleviation_scheme'
        db.delete_column('floodmaps_historicflood', 'alleviation_scheme')

        # Deleting field 'HistoricFlood.scheme_description'
        db.delete_column('floodmaps_historicflood', 'scheme_description')

        # Deleting field 'HistoricFlood.severity_index'
        db.delete_column('floodmaps_historicflood', 'severity_index')

        # Deleting field 'HistoricFlood.geographical_quality'
        db.delete_column('floodmaps_historicflood', 'geographical_quality_id')

        # Deleting field 'HistoricFlood.mapping_checked'
        db.delete_column('floodmaps_historicflood', 'mapping_checked')

        # Deleting field 'HistoricFlood.mapping_checked_date'
        db.delete_column('floodmaps_historicflood', 'mapping_checked_date')

        # Deleting field 'FloodAddress.townland'
        db.delete_column('floodmaps_floodaddress', 'townland_id')

        # Deleting field 'FloodAddress.town'
        db.delete_column('floodmaps_floodaddress', 'town_id')

        # Deleting field 'FloodAddress.county'
        db.delete_column('floodmaps_floodaddress', 'county_id')

        # Deleting field 'FloodAddress.name'
        db.delete_column('floodmaps_floodaddress', 'name')

        # Deleting field 'FloodAddress.building_number'
        db.delete_column('floodmaps_floodaddress', 'building_number')

        # Deleting field 'FloodAddress.street'
        db.delete_column('floodmaps_floodaddress', 'street')

        # Deleting field 'FloodAddress.easting'
        db.delete_column('floodmaps_floodaddress', 'easting')

        # Deleting field 'FloodAddress.northing'
        db.delete_column('floodmaps_floodaddress', 'northing')

        # Deleting field 'FloodAddress.grid_reference'
        db.delete_column('floodmaps_floodaddress', 'grid_reference')


    models = {
        'floodmaps.approvalstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'ApprovalStatus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
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
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
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
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
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
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
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
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
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