#write a python program to print a pattern using where the number of rows entered by the user.

n=int(input("enter the  number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()
