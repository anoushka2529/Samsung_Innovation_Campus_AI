import numpy as np
arr1=np.array([2,4,6])
arr2=np.array([2,4,6])
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr3=arr1
print(id(arr3))
arr1[0]=20
print(arr1)
print(arr3)
print(type(arr1))
arr4=np.copy(arr1)
print(id(arr4))
set1={1,2,3,4,5} #a set cannot have duplicate valaues
print(set1)
print(type(set1))
arr5=np.array(set1)
print(type(arr5))
dicti1={'A':'Apple',
        'B':'Banana'}
print(type(dicti1))
arr6=np.array(dicti1)
print(arr6)

print(np.arange(1000)) #stores as a list
print(np.arange(1,10,2)) #start,end,step
print(len(arr1))
arr8=np.array([15,'apple',10,'r'])
print(arr8)
print(type(arr8[0]))
print(type(arr8[1]))
print(type(arr8[3]))
arr9=np.array([15,'apple',True,2.5678])
print(arr9) 