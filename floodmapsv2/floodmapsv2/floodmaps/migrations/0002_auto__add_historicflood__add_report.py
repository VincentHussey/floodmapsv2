# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoricFlood'
        db.create_table('floodmaps_historicflood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('floodmaps', ['HistoricFlood'])

        # Adding M2M table for field report on 'HistoricFlood'
        db.create_table('floodmaps_historicflood_report', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('historicflood', models.ForeignKey(orm['floodmaps.historicflood'], null=False)),
            ('report', models.ForeignKey(orm['floodmaps.report'], null=False))
        ))
        db.create_unique('floodmaps_historicflood_report', ['historicflood_id', 'report_id'])

        # Adding model 'Report'
        db.create_table('floodmaps_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('report_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('file_name', self.gf('django.db.models.fields.files.FileField')(max_length=200)),
        ))
        db.send_create_signal('floodmaps', ['Report'])


    def backwards(self, orm):
        # Deleting model 'HistoricFlood'
        db.delete_table('floodmaps_historicflood')

        # Removing M2M table for field report on 'HistoricFlood'
        db.delete_table('floodmaps_historicflood_report')

        # Deleting model 'Report'
        db.delete_table('floodmaps_report')


    models = {
        'floodmaps.historicflood': {
            'Meta': {'object_name': 'HistoricFlood'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'report': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['floodmaps.Report']", 'symmetrical': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'floodmaps.report': {
            'Meta': {'object_name': 'Report'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['floodmaps']