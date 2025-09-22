import pandas as pd
import numpy as np
data1=pd.DataFrame({'Name':['Harry Potter','David Baker','John Smith',
                           'Juan Martinez','Jane Connor'],'Gender':['Male','Male','Male','Male','Female'],
                           'Age':[23,31,22,36,30]})
data2=pd.DataFrame({'Name':['John Smit','Alex Du Bois','Joanne Rowling',
                           'Jane Connor'],'Position':['Intern','Team Lead','Manager','Manager']
                           ,'Wage':[25000,75000,90000,70000]})

print(data1)
print(data2)
print(pd.merge(data1,data2,on='Name'))
print(pd.merge(data1,data2,left_on='Name',right_on='Name',how='left'))
print(pd.concat([data1,data2],sort=True))
print(pd.concat([data1,data2],axis=1,sort=True))