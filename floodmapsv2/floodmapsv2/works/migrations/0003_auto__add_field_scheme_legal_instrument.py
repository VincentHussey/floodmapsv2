# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Scheme.legal_instrument'
        db.add_column('works_scheme', 'legal_instrument',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['works.LegalInstrument']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Scheme.legal_instrument'
        db.delete_column('works_scheme', 'legal_instrument_id')


    models = {
        'works.benefitingland': {
            'Meta': {'ordering': "['scheme']", 'object_name': 'BenefitingLand'},
            'drained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.bridge': {
            'Meta': {'ordering': "['channel', 'ref']", 'object_name': 'Bridge'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Channel']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.channel': {
            'Meta': {'ordering': "['scheme', 'ref']", 'object_name': 'Channel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.channelsection': {
            'Meta': {'ordering': "['channel', 'name']", 'object_name': 'ChannelSection'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Channel']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.defendedarea': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'DefendedArea'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'effective_from': ('django.db.models.fields.DateTimeField', [], {}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.embankment': {
            'Meta': {'ordering': "['scheme', 'ref']", 'object_name': 'Embankment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.embankmentsection': {
            'Meta': {'ordering': "['embankment', 'name']", 'object_name': 'EmbankmentSection'},
            'embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Embankment']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.legalinstrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'LegalInstrument'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'works.pumpstation': {
            'Meta': {'ordering': "['scheme', 'name']", 'object_name': 'PumpStation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Scheme']"})
        },
        'works.scheme': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scheme'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_instrument': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.LegalInstrument']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'works.sluice': {
            'Meta': {'ordering': "['embankment', 'ref']", 'object_name': 'Sluice'},
            'embankment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Embankment']"}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['works']