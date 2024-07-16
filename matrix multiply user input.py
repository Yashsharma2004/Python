# MULTIPLICATION OF TWO MATRIX

import numpy as np

# user data
r1=int(input('number of rows in M1:'))
c1=int(input('number of columns in M1:'))
M1=[]
M2=[]
for i in range(r1):
    t=[]
    for j in range(c1):
        element=int(input(f'enter the element {i} x {j}  '))
        t.append(element)
    M1.append(t)
    
r2=int(input('number of rows in M2:'))
c2=int(input('number of columns in M2:'))
for i in range(r2):
    t=[]
    for j in range(c2):
        element=int(input(f'enter the element {i} x {j}  '))
        t.append(element)
    M2.append(t)

m1=np.array(M1)
m2=np.array(M2)
print('Matrix1')
print(m1)
print('\n Matrix2')
print(m2)

if m1.shape[1]==m2.shape[0]:
    out=np.dot(m1,m2)
    print('Multiplication')
    print(out)
else:
    print('Matrix are not valid for multiplication')
    


    