## 生成 Data/stockHolder 股票10大股东信息

import tushare as ts
import pandas as pd
import time
from lib import loginTusharePro
pro = loginTusharePro.login()


stockList = '../myData/stockList.csv'
a = pd.read_csv(stockList, encoding='utf-8')
for this_ts_code in a['ts_code']:
    df = pro.top10_holders(ts_code=this_ts_code,start_date='20170101', end_date='20171231')
    df.to_csv('../Data/stockHolder.csv', mode='a', header=None)
    time.sleep(3)
