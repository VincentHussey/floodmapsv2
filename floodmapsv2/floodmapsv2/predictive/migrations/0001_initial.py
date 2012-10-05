# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table('predictive_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['Status'])

        # Adding model 'VersionType'
        db.create_table('predictive_versiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['VersionType'])

        # Adding model 'Availability'
        db.create_table('predictive_availability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['Availability'])

        # Adding model 'UnitOfManagement'
        db.create_table('predictive_unitofmanagement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rbd', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['UnitOfManagement'])

        # Adding model 'AreaOfPotentialSignificantRisk'
        db.create_table('predictive_areaofpotentialsignificantrisk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.UnitOfManagement'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['AreaOfPotentialSignificantRisk'])

        # Adding model 'Climate'
        db.create_table('predictive_climate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['Climate'])

        # Adding model 'AnnualExceedanceProbability'
        db.create_table('predictive_annualexceedanceprobability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['AnnualExceedanceProbability'])

        # Adding model 'Source'
        db.create_table('predictive_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['Source'])

        # Adding model 'Scenario'
        db.create_table('predictive_scenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('climate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Climate'])),
            ('aep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.AnnualExceedanceProbability'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Source'])),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('predictive', ['Scenario'])

        # Adding model 'UncertaintyBand'
        db.create_table('predictive_uncertaintyband', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('predictive', ['UncertaintyBand'])

        # Adding model 'Node'
        db.create_table('predictive_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apsr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.AreaOfPotentialSignificantRisk'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['Node'])

        # Adding model 'NodeValue'
        db.create_table('predictive_nodevalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Scenario'])),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Node'])),
            ('elevation', self.gf('django.db.models.fields.FloatField')()),
            ('flow', self.gf('django.db.models.fields.FloatField')()),
            ('depth', self.gf('django.db.models.fields.FloatField')()),
            ('velocity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('predictive', ['NodeValue'])

        # Adding model 'FloodExtent'
        db.create_table('predictive_floodextent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apsr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.AreaOfPotentialSignificantRisk'])),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Scenario'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Status'])),
            ('version_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.VersionType'])),
            ('availability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.Availability'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['FloodExtent'])

        # Adding model 'Uncertainty'
        db.create_table('predictive_uncertainty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.FloodExtent'])),
            ('uncertainty_band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['predictive.UncertaintyBand'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(srid=2157)),
        ))
        db.send_create_signal('predictive', ['Uncertainty'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table('predictive_status')

        # Deleting model 'VersionType'
        db.delete_table('predictive_versiontype')

        # Deleting model 'Availability'
        db.delete_table('predictive_availability')

        # Deleting model 'UnitOfManagement'
        db.delete_table('predictive_unitofmanagement')

        # Deleting model 'AreaOfPotentialSignificantRisk'
        db.delete_table('predictive_areaofpotentialsignificantrisk')

        # Deleting model 'Climate'
        db.delete_table('predictive_climate')

        # Deleting model 'AnnualExceedanceProbability'
        db.delete_table('predictive_annualexceedanceprobability')

        # Deleting model 'Source'
        db.delete_table('predictive_source')

        # Deleting model 'Scenario'
        db.delete_table('predictive_scenario')

        # Deleting model 'UncertaintyBand'
        db.delete_table('predictive_uncertaintyband')

        # Deleting model 'Node'
        db.delete_table('predictive_node')

        # Deleting model 'NodeValue'
        db.delete_table('predictive_nodevalue')

        # Deleting model 'FloodExtent'
        db.delete_table('predictive_floodextent')

        # Deleting model 'Uncertainty'
        db.delete_table('predictive_uncertainty')


    models = {
        'predictive.annualexceedanceprobability': {
            'Meta': {'ordering': "['name']", 'object_name': 'AnnualExceedanceProbability'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.areaofpotentialsignificantrisk': {
            'Meta': {'ordering': "['name']", 'object_name': 'AreaOfPotentialSignificantRisk'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.UnitOfManagement']"})
        },
        'predictive.availability': {
            'Meta': {'ordering': "['name']", 'object_name': 'Availability'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.climate': {
            'Meta': {'ordering': "['name']", 'object_name': 'Climate'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.floodextent': {
            'Meta': {'ordering': "['apsr']", 'object_name': 'FloodExtent'},
            'apsr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AreaOfPotentialSignificantRisk']"}),
            'availability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Availability']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Scenario']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Status']"}),
            'version_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.VersionType']"})
        },
        'predictive.node': {
            'Meta': {'ordering': "['name']", 'object_name': 'Node'},
            'apsr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AreaOfPotentialSignificantRisk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.nodevalue': {
            'Meta': {'ordering': "['node']", 'object_name': 'NodeValue'},
            'depth': ('django.db.models.fields.FloatField', [], {}),
            'elevation': ('django.db.models.fields.FloatField', [], {}),
            'flow': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Node']"}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Scenario']"}),
            'velocity': ('django.db.models.fields.FloatField', [], {})
        },
        'predictive.scenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'aep': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AnnualExceedanceProbability']"}),
            'climate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Climate']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Source']"})
        },
        'predictive.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.status': {
            'Meta': {'ordering': "['name']", 'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.uncertainty': {
            'Meta': {'ordering': "['extent']", 'object_name': 'Uncertainty'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.FloodExtent']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uncertainty_band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.UncertaintyBand']"})
        },
        'predictive.uncertaintyband': {
            'Meta': {'ordering': "['name']", 'object_name': 'UncertaintyBand'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.unitofmanagement': {
            'Meta': {'ordering': "['name']", 'object_name': 'UnitOfManagement'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rbd': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'predictive.versiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'VersionType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['predictive']