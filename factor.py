#write a program to display factors of given interger


num=int(input("enter  no.:"))
for i in range(1,num+1):
    if num % i ==0:
        print(i,end=' ')
