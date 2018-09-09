## 生成 Data/stockList 所有股票名称

from lib import loginTusharePro
pro = loginTusharePro.login()


data = pro.stock_basic(exchange_id='', is_hs='', fields='ts_code,symbol,name,exchange_id,list_date,list_status')
data.to_csv('../myData/stockList.csv')