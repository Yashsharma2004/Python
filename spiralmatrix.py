# SPIRAL MATRIX
#3 4
#3 5 3 2
#1 2 4 6 
#7 2 6 4 
    
R,C=list(map(int,input().split()))
M=[]
for i in range(R):
    M.append(list(map(int,input().split())))

for i in M:
    print(*i)
print()
    
t=0
b=R-1
l=0
r=C-1
d=0
out=[]
while t<=b and l<=r:
    if d==0:
        for i in range(l,r+1):
            out.append(M[t][i])
        d=1
        t+=1
    elif d==1:
        for i in range(t,b+1):
            out.append(M[i][r])
        d=2
        r-=1
    elif d==2:
        for i in range(r,l-1,-1):
            out.append(M[b][i])
        d=3
        b-=1
    elif d==3:
        for i in range(b,t-1,-1):
            out.append(M[i][l])
        d=0
        l+=1
print(*out)
