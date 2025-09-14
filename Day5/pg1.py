import numpy as np
mat1=np.array([[21,0,0],[0,87,0],[0,0,58]])
mat2=np.array([[21,1,0],[10,87,56],[66,78,58]])
print(mat1+mat2)
print(mat1-(1/2)*mat2)
print(5*mat1)

print("Addition of the two matrices are\n",mat1+mat2)
mult = np.array(mat1)
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mult[i][j] = mat1[i][j] * mat2[i][j]
print("Element-wise multiplication of the two matrices:\n", mult) 
detA=np.linalg.det(mat1)   #linear algebra functionalities
print(detA)                   
Ainv=np.linalg.inv(mat1)
print(Ainv)
detB=np.linalg.det(mat2)
print(detB)
print("Rank of mat1:", np.linalg.matrix_rank(mat1))
print(np.dot(mat1,mat2))
print(np.dot(mat2,mat1))