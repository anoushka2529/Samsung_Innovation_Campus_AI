import numpy as np
import pandas as pd
my_header=['a','b','c']
my_index_out=['G1']*3 + ['G2']*3 # '*' symbolises copy
my_index_in=[1,2,3]*2
my_index_zipped=list(zip(my_index_out,my_index_in))
my_index=pd.MultiIndex.from_tuples(my_index_zipped)
df=pd.DataFrame(data=np.random.randn(6,3),index=my_index,columns=my_header)
print(df)
