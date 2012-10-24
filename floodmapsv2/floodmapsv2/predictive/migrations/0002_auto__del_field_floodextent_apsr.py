# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FloodExtent.apsr'
        db.delete_column('predictive_floodextent', 'apsr_id')

        # Adding M2M table for field apsr on 'FloodExtent'
        db.create_table('predictive_floodextent_apsr', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('floodextent', models.ForeignKey(orm['predictive.floodextent'], null=False)),
            ('areaofpotentialsignificantrisk', models.ForeignKey(orm['predictive.areaofpotentialsignificantrisk'], null=False))
        ))
        db.create_unique('predictive_floodextent_apsr', ['floodextent_id', 'areaofpotentialsignificantrisk_id'])


    def backwards(self, orm):
        # Adding field 'FloodExtent.apsr'
        db.add_column('predictive_floodextent', 'apsr',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['predictive.AreaOfPotentialSignificantRisk']),
                      keep_default=False)

        # Removing M2M table for field apsr on 'FloodExtent'
        db.delete_table('predictive_floodextent_apsr')


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
            'Meta': {'object_name': 'FloodExtent'},
            'apsr': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['predictive.AreaOfPotentialSignificantRisk']", 'null': 'True', 'blank': 'True'}),
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