import datetime
import pandas_datareader as pdr
import pandas as pd

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2020,1,1)

writer = pd.ExcelWriter('stock.xlsx')

pdr.get_data_yahoo('012330.KS',start,end).to_excel(writer,sheet_name = '삼성전자')
pdr.get_data_yahoo('000660.KS',start,end).to_excel(writer,sheet_name = 'SK하이닉스')
pdr.get_data_yahoo('035420.KS',start,end).to_excel(writer,sheet_name = 'NAVER')
pdr.get_data_yahoo('051910.KS',start,end).to_excel(writer,sheet_name = 'LG화학')
pdr.get_data_yahoo('005490.KS',start,end).to_excel(writer,sheet_name = 'POSCO')
pdr.get_data_yahoo('055550.KS',start,end).to_excel(writer,sheet_name = '신한지주')
pdr.get_data_yahoo('105560.KS',start,end).to_excel(writer,sheet_name = 'KB금융')
pdr.get_data_yahoo('036570.KS',start,end).to_excel(writer,sheet_name = '엔씨소프트')
pdr.get_data_yahoo('090430.KS',start,end).to_excel(writer,sheet_name = '아모레퍼시픽')
pdr.get_data_yahoo('012330.KS',start,end).to_excel(writer,sheet_name = '현대모비스')
writer.save()