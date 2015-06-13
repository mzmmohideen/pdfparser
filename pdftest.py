# import pandas as pd
import json
from django.http import HttpResponse
import pdftableextract as pdf
def table_extract():
	print 'working'
	pages = ["1"]
	cells = [pdf.process_page("/home/nizam/Downloads/TNDS3328_23122014_CNNSEEQ_1.pdf",p) for p in pages]
	cells = [item for sublist in cells for item in sublist]
	li = pdf.table_to_list(cells, pages)[1]
	user_header = li[0][0].split(':')
	user_header_data = {'contract_note_no':user_header[1].split(' ')[1],'settlement_no':user_header[2].split(' ')[1],'trade_date':user_header[3].split(' ')[1],'unique_client_code_no':user_header[5].split(' ')[1],'trading_code_no':user_header[7].split(' ')[1]}
	for i in li:
		if 'ORDER NO' in i[2]:  start = li.index(i)
		if 'Sub Total' in i[2]: end = li.index(i)	
	tot_list = [li[i] for i in range(start,end)]
	# data = map(lambda x:{'ORDER NO.':x[2],'ORDER TIME':x[5],'TRADE NO.':x[6],'TRADE TIME':x[7],'SECURITY (CONTRACT DESCRIPTION)':x[8],'Quantity Bought for you':x[10],'Quantity Sold for you':x[11],'Gross Rate per Unit (Rs.)':x[13],'Gross Total (Rs.)':x[17],'Brokerage Total (Rs.)':x[18],'Service Tax* (Total) (Rs.)':x[19],'Securities Transaction Tax (Rs.)':x[20],'Net Value Gr. Value(+/-)Brok. (Rs.)':x[22]},tot_list[1:])
	data = filter(lambda x: any(x.values()),map(lambda x:{'order_no':x[2],'order_time':x[5],'trade_no':x[6],'trade_time':x[7],'security':x[8],'quantity_bought':x[10],'quantity_sold':x[11],'gross_rate':x[13],'gross_total':x[17],'brokerage_total':x[18],'service_tax':x[19],'securities_transaction_tax':x[20],'net_value':x[22]},tot_list[1:]))
	data_dict = {'user_table_data':data,'user_header_data':user_header_data}	
	return data_dict
	# f = open("content.txt","w")
	# print >>f,data_dict
	# f.close()

# if __name__ == '__main__':
# 	table_extract()
