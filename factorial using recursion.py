def fact(n):
 if n<0:
  print("Enter positive num")

 elif n==0 or n==1:
   return 1
 else :
    return n*fact(n-1)
n= int(input("Enter a num :"))
print(fact(n))
 

 