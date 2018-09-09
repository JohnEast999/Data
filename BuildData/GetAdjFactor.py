#得到复权因子

from lib import loginTusharePro
pro = loginTusharePro.login()

df = pro.adj_factor(ts_code='000001.SZ', trade_date='')

# print(type(df))
print(df)