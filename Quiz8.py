import numpy as np
n = int(input('Create square matrix : '))           #กำหนดขนาดของ Matrix
A = np.ones(n*n).reshape((n,n)) #กำหนดค่า1ในmatrix
for i in range(0,n):       #กำหนดเงื่อนไขให้เป็นไปตามโจทย์
    for j in range(0,n):
        if(i < j and j != n):
            A[i,j] = 0
        elif(i == j or j == n):                                 
            A[i,j] =  1                                          
        else:                                                   
            A[i,j] =  -1                                         
print(A)                           #3แสดงค่าmatrix



