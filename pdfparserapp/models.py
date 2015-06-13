from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

class user_pdf_parse(models.Model):
	contract_note_no = models.CharField(max_length=50,null = True, blank = True)
	settlement_no = models.CharField(max_length=50,null = True, blank = True)
	trade_date = models.DateTimeField(max_length=50,default=timezone.now)
	unique_client_code_no = models.CharField(max_length=50,unique = True)
	trading_code_no = models.CharField(max_length=50,null = True, blank = True)

class user_pdf_data(models.Model):
	user = models.ForeignKey(user_pdf_parse)
	order_no = models.CharField(max_length=100,null = True, blank = True)
	order_time = models.CharField(max_length=100,null = True, blank = True)
	trade_no = models.CharField(max_length=100,null = True, blank = True)
	trade_time = models.CharField(max_length=100,null = True, blank = True)
	security = models.CharField(max_length=100,null = True, blank = True)
	quantity_bought = models.CharField(max_length=100,null = True, blank = True)
	quantity_sold = models.CharField(max_length=100,null = True, blank = True)
	gross_rate = models.CharField(max_length=100,null = True, blank = True)
	gross_total = models.CharField(max_length=100,null = True, blank = True)
	brokerage_total = models.CharField(max_length=100,null = True, blank = True)
	service_tax = models.CharField(max_length=100,null = True, blank = True)
	securities_transaction_tax = models.CharField(max_length=100,null = True, blank = True)
	net_value = models.CharField(max_length=100,null = True, blank = True)

# Create your models here.
