# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FloodSourceType'
        db.create_table('floodmaps_floodsourcetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodSourceType'])

        # Adding model 'FloodReportLink'
        db.create_table('floodmaps_floodreportlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.HistoricFlood'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Report'], null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodReportLink'])

        # Adding model 'QualityCode'
        db.create_table('floodmaps_qualitycode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['QualityCode'])

        # Adding model 'FloodGroup'
        db.create_table('floodmaps_floodgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.FloodGroupType'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodGroup'])

        # Adding model 'FloodGroupType'
        db.create_table('floodmaps_floodgrouptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodGroupType'])

        # Adding model 'ReportInterpretation'
        db.create_table('floodmaps_reportinterpretation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Report'])),
            ('quality_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.QualityCode'])),
            ('interpretation_stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.InterpretationStage'])),
            ('stage_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('justification', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('floodmaps', ['ReportInterpretation'])

        # Adding model 'FloodCause'
        db.create_table('floodmaps_floodcause', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodCause'])

        # Adding model 'FloodRecordType'
        db.create_table('floodmaps_floodrecordtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodRecordType'])

        # Adding model 'InterpretationStage'
        db.create_table('floodmaps_interpretationstage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('floodmaps', ['InterpretationStage'])

        # Adding model 'ReportType'
        db.create_table('floodmaps_reporttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('initial', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('default_extension', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('default_folder', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['ReportType'])

        # Adding model 'FloodCauseLink'
        db.create_table('floodmaps_floodcauselink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.HistoricFlood'])),
            ('cause', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.FloodCause'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Report'], null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodCauseLink'])

        # Adding model 'ApprovalStatus'
        db.create_table('floodmaps_approvalstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['ApprovalStatus'])

        # Adding model 'Glossary'
        db.create_table('floodmaps_glossary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.GlossaryCategory'])),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('floodmaps', ['Glossary'])

        # Adding model 'HistoricFloodInterpretation'
        db.create_table('floodmaps_historicfloodinterpretation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.HistoricFlood'])),
            ('quality_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.QualityCode'])),
            ('stage_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('justification', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('floodmaps', ['HistoricFloodInterpretation'])

        # Adding model 'DataSource'
        db.create_table('floodmaps_datasource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('initial', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('default_folder', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('floodmaps', ['DataSource'])

        # Adding model 'GlossaryCategory'
        db.create_table('floodmaps_glossarycategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('floodmaps', ['GlossaryCategory'])

        # Adding model 'ReportAddress'
        db.create_table('floodmaps_reportaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Report'])),
        ))
        db.send_create_signal('floodmaps', ['ReportAddress'])

        # Adding model 'FloodAddress'
        db.create_table('floodmaps_floodaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.HistoricFlood'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.Report'], null=True, blank=True)),
        ))
        db.send_create_signal('floodmaps', ['FloodAddress'])

        # Adding M2M table for field group on 'HistoricFlood'
        db.create_table('floodmaps_historicflood_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('historicflood', models.ForeignKey(orm['floodmaps.historicflood'], null=False)),
            ('floodgroup', models.ForeignKey(orm['floodmaps.floodgroup'], null=False))
        ))
        db.create_unique('floodmaps_historicflood_group', ['historicflood_id', 'floodgroup_id'])

        # Adding field 'Report.report_type'
        db.add_column('floodmaps_report', 'report_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['floodmaps.ReportType'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FloodSourceType'
        db.delete_table('floodmaps_floodsourcetype')

        # Deleting model 'FloodReportLink'
        db.delete_table('floodmaps_floodreportlink')

        # Deleting model 'QualityCode'
        db.delete_table('floodmaps_qualitycode')

        # Deleting model 'FloodGroup'
        db.delete_table('floodmaps_floodgroup')

        # Deleting model 'FloodGroupType'
        db.delete_table('floodmaps_floodgrouptype')

        # Deleting model 'ReportInterpretation'
        db.delete_table('floodmaps_reportinterpretation')

        # Deleting model 'FloodCause'
        db.delete_table('floodmaps_floodcause')

        # Deleting model 'FloodRecordType'
        db.delete_table('floodmaps_floodrecordtype')

        # Deleting model 'InterpretationStage'
        db.delete_table('floodmaps_interpretationstage')

        # Deleting model 'ReportType'
        db.delete_table('floodmaps_reporttype')

        # Deleting model 'FloodCauseLink'
        db.delete_table('floodmaps_floodcauselink')

        # Deleting model 'ApprovalStatus'
        db.delete_table('floodmaps_approvalstatus')

        # Deleting model 'Glossary'
        db.delete_table('floodmaps_glossary')

        # Deleting model 'HistoricFloodInterpretation'
        db.delete_table('floodmaps_historicfloodinterpretation')

        # Deleting model 'DataSource'
        db.delete_table('floodmaps_datasource')

        # Deleting model 'GlossaryCategory'
        db.delete_table('floodmaps_glossarycategory')

        # Deleting model 'ReportAddress'
        db.delete_table('floodmaps_reportaddress')

        # Deleting model 'FloodAddress'
        db.delete_table('floodmaps_floodaddress')

        # Removing M2M table for field group on 'HistoricFlood'
        db.delete_table('floodmaps_historicflood_group')

        # Deleting field 'Report.report_type'
        db.delete_column('floodmaps_report', 'report_type_id')


    models = {
        'floodmaps.approvalstatus': {
            'Meta': {'object_name': 'ApprovalStatus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'floodmaps.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'default_folder': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodaddress': {
            'Meta': {'object_name': 'FloodAddress'},
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']", 'null': 'True', 'blank': 'True'})
        },
        'floodmaps.floodcause': {
            'Meta': {'object_name': 'FloodCause'},
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
            'Meta': {'object_name': 'FloodGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.FloodGroupType']"})
        },
        'floodmaps.floodgrouptype': {
            'Meta': {'object_name': 'FloodGroupType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.floodrecordtype': {
            'Meta': {'object_name': 'FloodRecordType'},
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
            'Meta': {'object_name': 'FloodSourceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.glossary': {
            'Meta': {'object_name': 'Glossary'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.GlossaryCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'floodmaps.glossarycategory': {
            'Meta': {'object_name': 'GlossaryCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'floodmaps.historicflood': {
            'Meta': {'object_name': 'HistoricFlood'},
            'cause': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.FloodCause']", 'through': "orm['floodmaps.FloodCauseLink']", 'symmetrical': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['floodmaps.FloodGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'report': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.Report']", 'symmetrical': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.historicfloodinterpretation': {
            'Meta': {'object_name': 'HistoricFloodInterpretation'},
            'flood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.HistoricFlood']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justification': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quality_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.QualityCode']"}),
            'stage_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.interpretationstage': {
            'Meta': {'object_name': 'InterpretationStage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'floodmaps.qualitycode': {
            'Meta': {'object_name': 'QualityCode'},
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
            'Meta': {'object_name': 'ReportAddress'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']"})
        },
        'floodmaps.reportinterpretation': {
            'Meta': {'object_name': 'ReportInterpretation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interpretation_stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.InterpretationStage']"}),
            'justification': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quality_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.QualityCode']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['floodmaps.Report']"}),
            'stage_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.reporttype': {
            'Meta': {'object_name': 'ReportType'},
            'default_extension': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'default_folder': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['floodmaps']