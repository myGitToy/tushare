# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
def data_update():
    df = ts.get_k_data('510500', start='2015-02-21',end='2016-03-01',ktype='D',autype='qfq')  #work
    print(df)

def data_timeToMarket(stock_id=''):
    df = ts.get_stock_basics()
    date = df.ix[stock_id]['timeToMarket'] #上市日期YYYYMMDD
    print(date)
data_timeToMarket("300223")

