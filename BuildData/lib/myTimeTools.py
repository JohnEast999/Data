#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: JohnEast

import datetime

def getDateFromCsvOneLine(oneLine):
    lastTradeDate_series = oneLine['trade_date']
    lastTradeDate = datetime.datetime.strptime(lastTradeDate_series.to_string()[6:], "%Y%m%d").date()
    return lastTradeDate

def dateToString(date):
    stringdate = date.strftime('%Y%m%d')
    return stringdate

def ifDate1AfterDate2(date1,date2):
    if date1 > date2:
        return True
    return False

def xDaysAfterTheDate(date, x):
    xDaysAfter = date + datetime.timedelta(days=x)
    return xDaysAfter