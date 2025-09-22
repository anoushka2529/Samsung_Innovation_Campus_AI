import pandas as pd
data1=pd.read_csv('korean_stocks_financials_less.xlsx')
data2=pd.read_csv('korean_stocks_financials.xlsx')
data3=pd.read_csv('korean_stocks_numeric_values_less.xlsx')
data4=pd.read_csv('korean_stocks_numeric_values.xlsx')

print(pd.merge(data1,data2,data3,data4,on='id'))
print(pd.merge(data1,data2,left_on='id',right_on='stock_name',how='left'))
print(pd.merge(data1,data2,left_on='id',right_on='stock_name',how='right'))
print(pd.merge(data1,data2,left_on='id',right_on='stock_name',how='outer'))

print(pd.concat([data1,data2],sort=True))
print(pd.concat([data1,data2],axis=1,sort=True))