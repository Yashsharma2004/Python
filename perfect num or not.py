num=int(input("enter no.:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("perfect no.")
else:
    print("not a perfect no.")            