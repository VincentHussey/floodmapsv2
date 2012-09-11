# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HistoricFlood.flood_record_type'
        db.add_column('floodmaps_historicflood', 'flood_record_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.FloodRecordType'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HistoricFlood.flood_record_type'
        db.delete_column('floodmaps_historicflood', 'flood_record_type_id')


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
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']", 'null': 'True', 'blank': 'True'})
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
            'cause': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.FloodCause']", 'through': "orm['floodmaps.FloodCauseLink']", 'symmetrical': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'flood_record_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodRecordType']", 'null': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['floodmaps.FloodGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'report': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.Report']", 'symmetrical': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']"})
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
        }
    }

    complete_apps = ['floodmaps']