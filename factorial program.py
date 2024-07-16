a=1
n=int(input("Enter a num :"))
if n<0:
  print("Enter num greater than 0")
elif n==0 or n==1:
    print(a)
else :
    for i in range (2,n+1):
      a=a*i
print(a)      
