## 生成 myData/stockPriceAmount/ stockID.csv 文件
from lib import loginTusharePro
pro = loginTusharePro.login()

import os
import pandas as pd
from datetime import date
from lib import myTimeTools

# test_ts_code = '000001.SZ'

stockListCsv = '../myData/stockList.csv'
stockList = pd.read_csv(stockListCsv, encoding='utf-8')

date_today = date.today()



def addData(tsCode,listDate):
    path = '../myData/stockHistoryNotAdjusted/' + tsCode + '.csv'
    fileExist_bool = os.path.exists(path)

    if fileExist_bool:
        thisCodeData = pd.read_csv(path)
        lastTradeDate = myTimeTools.getDateFromCsvOneLine(thisCodeData.tail(1))

        if myTimeTools.ifDate1AfterDate2(date_today, lastTradeDate):
            date_onedayAfterLastTrade = myTimeTools.xDaysAfterTheDate(lastTradeDate, 1)

            startDate = myTimeTools.dateToString(date_onedayAfterLastTrade)
            endDate = myTimeTools.dateToString(date_today)
            dataShouldAdd = pro.daily(ts_code=tsCode, start_date=startDate, end_date=endDate).iloc[::-1]
            dataShouldAdd.to_csv(path, mode='a', header= None)
    else:
        startDate = listDate
        endDate = myTimeTools.dateToString(date_today)
        newData = pro.daily(ts_code=tsCode, start_date=startDate, end_date=endDate).iloc[::-1]
        newData.to_csv(path)

for index, row in stockList.iterrows():
    thisTsCode = row['ts_code']
    thisListDate = row['list_date']
    addData(thisTsCode, thisListDate)
