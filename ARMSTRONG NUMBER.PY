n =int(input("enter any no.:"))
sum=0
num=n
length =len(str(n))
for i in range(length):
  digit=n%10
  sum +=(digit**length)
  n//=10
if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")