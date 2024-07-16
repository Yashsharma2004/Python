#Write a python program to take two 3x3 matrix from user and add them

l1=[]
a=[]
for i in range (0,3):
    l1=list(map(int,input().split()))
    a.append(l1)

l1=[]
b=[]
for i in range (0,3):
    l1=list(map(int,input().split()))
    b.append(l1)

c=[]
for i in range (0,3):
        c1=[0,0,0]
        for j in range(0,3):
            c1[j]=a[i][j]+b[i][j]
        c.append(c1)
for i in c:
        print(i)
