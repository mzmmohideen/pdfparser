from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from pdfparserapp.models import *
from pdftest import table_extract
import json

def pdf_parse_data_feed(request):
	get_data = table_extract()
	print 'get_data',get_data['user_header_data']
	user_header_data = get_data['user_header_data']
	user_table_data = get_data['user_table_data']
	add_user = user_pdf_parse.objects.create(contract_note_no=user_header_data['contract_note_no'],settlement_no = user_header_data['settlement_no'],trade_date = user_header_data['trade_date'],unique_client_code_no = user_header_data['unique_client_code_no'],trading_code_no = user_header_data['trading_code_no'])
	add_data = user_pdf_data.objects.create(user = add_user,order_no = user_table_data['order_no'],order_time = user_table_data['order_time'],trade_no = user_table_data['trade_no'],trade_time = user_table_data['trade_time'],security = user_table_data['security'],quantity_bought = user_table_data['quantity_bought'],quantity_sold = user_table_data['quantity_sold'],gross_rate = user_table_data['gross_rate'],gross_total = user_table_data['gross_total'],brokerage_total = user_table_data['brokerage_total'],service_tax = user_table_data['service_tax'],securities_transaction_tax = user_table_data['securities_transaction_tax'],net_value = user_table_data['net_value'])
	return HttpResponse(content=json.dumps(get_data),content_type='Application/json')

# Create your views here.
