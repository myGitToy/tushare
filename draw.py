# -*- coding: utf-8 -*-
import tushare as ts  
print(ts.__version__)
df = ts.get_k_data('510300')
idx=df.tail(5).index
for n in idx:
    print("交易日%s,收盘价%s" % (df.loc[n].date,df.loc[n].close))