# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IndicativeFloodDataset'
        db.create_table('indicative_indicativeflooddataset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('metadata', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('indicative', ['IndicativeFloodDataset'])

        # Adding model 'IndicativeFloodCategory'
        db.create_table('indicative_indicativefloodcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indicative', ['IndicativeFloodCategory'])

        # Adding model 'IndicativeFlood'
        db.create_table('indicative_indicativeflood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicative.IndicativeFloodDataset'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicative.IndicativeFloodCategory'])),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('indicative', ['IndicativeFlood'])


    def backwards(self, orm):
        # Deleting model 'IndicativeFloodDataset'
        db.delete_table('indicative_indicativeflooddataset')

        # Deleting model 'IndicativeFloodCategory'
        db.delete_table('indicative_indicativefloodcategory')

        # Deleting model 'IndicativeFlood'
        db.delete_table('indicative_indicativeflood')


    models = {
        'indicative.indicativeflood': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFlood'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicative.IndicativeFloodCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicative.IndicativeFloodDataset']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'indicative.indicativefloodcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFloodCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'indicative.indicativeflooddataset': {
            'Meta': {'ordering': "['name']", 'object_name': 'IndicativeFloodDataset'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['indicative']