'''Matrices are used in image processing and transpose of a matrix is used when we change the orientation of the image'''
'''import numpy as np
mat1=np.array([[21,0,0],[0,87,0],[0,0,58]])
mat2=np.array([[21,1,0],[10,87,56],[66,78,58]])
print("The matrix is a: Diagonal matrix \n",mat1)3
print("The matrix is a: Square matrix ",mat2)'''

import numpy as np
print("Enter the number of rows and columns for the matrix: ")
row = int(input())
colu = int(input())
print("Enter the matrix elements")
matr = np.zeros((row, colu))
for i in range(row):
    for j in range(colu):
        matr[i][j] = int(input())

print("Matrix entered:\n", matr)

if row==colu:
    print("Square matrix")
if row == colu and np.array_equal(matr, matr.T):
    print("Symmetric matrix")
else:
    print("none")