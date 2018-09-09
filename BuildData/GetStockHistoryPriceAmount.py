## 生成 myData/stockPriceAmount/ stockID.csv 文件

from lib import loginTusharePro
pro = loginTusharePro.login()


ts_code = '000001.SZ'
data = pro.daily(ts_code=ts_code, start_date='20180701', end_date='20180718')

# data.to_csv('../myData/stockHistory/'+ts_code+'.csv')

