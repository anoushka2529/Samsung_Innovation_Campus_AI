import numpy as np
import pandas as pd
student1=pd.Series({'kor':100,'eng':90,'math':80})
print(student1)
s1=pd.Series({'kor':100,'eng':90,'math':80})
s2=pd.Series({'eng':90,'kor':100,'math':80})
addn=s1+s2
sub=s1-s2
mult=s1*s2
div=s1/s2
print(addn)
print(type(addn))
print(sub)
print(mult)
print(div)
import pandas as pd
data=pd.DataFrame({'kor':[100,90,80],'eng':[90,80,70],'math':[80,70,60]})
data1=pd.DataFrame({'addn','sub','mult','div'})
print(data1)
print(data)
import pandas as pd
import numpy as np

s1 = pd.Series({'kor': np.nan, 'eng': 80, 'math': 90})
s2 = pd.Series({'math': 80, 'kor': 90})

sr_add  = s1.add(s2, fill_value=0)
sr_sub  = s1.sub(s2, fill_value=0)
sr_mult = s1.mul(s2, fill_value=0)   # <-- corrected here
sr_div  = s1.div(s2, fill_value=0)

print("success")
print("Addition:\n", sr_add)
print("Subtraction:\n", sr_sub)
print("Multiplication:\n", sr_mult)
print("Division:\n", sr_div)