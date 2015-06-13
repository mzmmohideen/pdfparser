# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'user_pdf_parse'
        db.create_table(u'pdfparserapp_user_pdf_parse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contract_note_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('settlement_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('trade_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, max_length=50)),
            ('unique_client_code_no', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('trading_code_no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'pdfparserapp', ['user_pdf_parse'])

        # Adding model 'user_pdf_data'
        db.create_table(u'pdfparserapp_user_pdf_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdfparserapp.user_pdf_parse'])),
            ('order_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('order_time', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('trade_no', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('trade_time', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('security', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('quantity_bought', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('quantity_sold', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gross_rate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gross_total', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('brokerage_total', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('service_tax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('securities_transaction_tax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('net_value', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'pdfparserapp', ['user_pdf_data'])


    def backwards(self, orm):
        # Deleting model 'user_pdf_parse'
        db.delete_table(u'pdfparserapp_user_pdf_parse')

        # Deleting model 'user_pdf_data'
        db.delete_table(u'pdfparserapp_user_pdf_data')


    models = {
        u'pdfparserapp.user_pdf_data': {
            'Meta': {'object_name': 'user_pdf_data'},
            'brokerage_total': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gross_rate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gross_total': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'quantity_bought': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'quantity_sold': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'securities_transaction_tax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'security': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service_tax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trade_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trade_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pdfparserapp.user_pdf_parse']"})
        },
        u'pdfparserapp.user_pdf_parse': {
            'Meta': {'object_name': 'user_pdf_parse'},
            'contract_note_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'settlement_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trade_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'max_length': '50'}),
            'trading_code_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'unique_client_code_no': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['pdfparserapp']