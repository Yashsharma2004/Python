


a=int(input("enter the 3 digit no.:"))
b=(a%10)*100
a=a//10
b=b+(a%10)*10
a=a//10
b=b+a
print(b)


