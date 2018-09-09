## 生成 myData/stockPriceAmount/ stockID.csv 文件
from lib import loginTusharePro
pro = loginTusharePro.login()

import os
import pandas as pd
from datetime import date
import datetime
from lib import myTimeTools

test_ts_code = '000001.SZ'
# data = pro.daily(ts_code=ts_code, start_date='20180701', end_date='20180718')

stockListCsv = '../myData/stockList.csv'
stockList = pd.read_csv(stockListCsv, encoding='utf-8')

date_today = date.today()

for thisTsCode in stockList['ts_code']:
    pass


def addData(tsCode):
    path = '../myData/stockHistory/' + tsCode + '.csv'
    fileExist_bool = os.path.exists(path)

    if fileExist_bool:
        thisCodeData = pd.read_csv(path)
        lastTradeDate = myTimeTools.getDateFromCsvOneLine(thisCodeData.tail(1))

        if myTimeTools.ifDate1AfterDate2(date_today, lastTradeDate):
            date_onedayAfterLastTrade = myTimeTools.xDaysAfterTheDate(lastTradeDate, 1)

            startDate = myTimeTools.dateToString(date_onedayAfterLastTrade)
            endDate = myTimeTools.dateToString(date_today)
            dataShouldAdd = pro.daily(ts_code=tsCode, start_date=startDate, end_date=endDate).iloc[::-1]
            print(dataShouldAdd)

    else:

        pass
        # print(thisTsCode + ' if exists: '+ str(fileExist_bool))

addData(test_ts_code)