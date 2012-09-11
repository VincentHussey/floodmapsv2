# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coast'
        db.create_table('geography_coast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['Coast'])

        # Adding model 'Province'
        db.create_table('geography_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_sq_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimiter_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['Province'])

        # Adding model 'County'
        db.create_table('geography_county', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('irish_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['County'])

        # Adding model 'DistrictElectoralDivision'
        db.create_table('geography_districtelectoraldivision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.County'])),
        ))
        db.send_create_signal('geography', ['DistrictElectoralDivision'])

        # Adding model 'Town'
        db.create_table('geography_town', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_and_county', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.County'])),
            ('centroid_x', self.gf('django.db.models.fields.FloatField')()),
            ('centroid_y', self.gf('django.db.models.fields.FloatField')()),
            ('irish_name', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('irish_class', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('town_category', self.gf('django.db.models.fields.IntegerField')()),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('geography', ['Town'])

        # Adding model 'Townland'
        db.create_table('geography_townland', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('os_townland_id', self.gf('django.db.models.fields.IntegerField')()),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.County'])),
            ('ded', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.DistrictElectoralDivision'])),
            ('upper', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('geography', ['Townland'])

        # Adding model 'CoastalWater'
        db.create_table('geography_coastalwater', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('geography', ['CoastalWater'])

        # Adding model 'Catchment'
        db.create_table('geography_catchment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_sq_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimiter_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('hydrometric_area', self.gf('django.db.models.fields.IntegerField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['Catchment'])

        # Adding model 'Road'
        db.create_table('geography_road', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mapflow_id', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('approx_region', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geosid', self.gf('django.db.models.fields.FloatField')()),
            ('nra_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('code', self.gf('django.db.models.fields.FloatField')()),
            ('fre', self.gf('django.db.models.fields.FloatField')()),
            ('approx_region_city_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('town', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Town'])),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['Road'])

        # Adding model 'Lake'
        db.create_table('geography_lake', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seg_cd', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('area_sq_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimiter_km', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('hydrometric_area', self.gf('django.db.models.fields.IntegerField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['Lake'])

        # Adding model 'River'
        db.create_table('geography_river', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('epa_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('catchment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Catchment'])),
            ('flow_direction', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('up_stream_length', self.gf('django.db.models.fields.FloatField')()),
            ('down_stream_length', self.gf('django.db.models.fields.FloatField')()),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('geography', ['River'])


    def backwards(self, orm):
        # Deleting model 'Coast'
        db.delete_table('geography_coast')

        # Deleting model 'Province'
        db.delete_table('geography_province')

        # Deleting model 'County'
        db.delete_table('geography_county')

        # Deleting model 'DistrictElectoralDivision'
        db.delete_table('geography_districtelectoraldivision')

        # Deleting model 'Town'
        db.delete_table('geography_town')

        # Deleting model 'Townland'
        db.delete_table('geography_townland')

        # Deleting model 'CoastalWater'
        db.delete_table('geography_coastalwater')

        # Deleting model 'Catchment'
        db.delete_table('geography_catchment')

        # Deleting model 'Road'
        db.delete_table('geography_road')

        # Deleting model 'Lake'
        db.delete_table('geography_lake')

        # Deleting model 'River'
        db.delete_table('geography_river')


    models = {
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
        'geography.coast': {
            'Meta': {'ordering': "['attribute']", 'object_name': 'Coast'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'geography.province': {
            'Meta': {'ordering': "['name']", 'object_name': 'Province'},
            'area_sq_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'perimiter_km': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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
        'geography.road': {
            'Meta': {'ordering': "['name']", 'object_name': 'Road'},
            'approx_region': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'approx_region_city_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.FloatField', [], {}),
            'fre': ('django.db.models.fields.FloatField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'geosid': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapflow_id': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nra_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Town']"})
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

    complete_apps = ['geography']