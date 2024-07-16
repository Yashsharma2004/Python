n=int(input("enter the no.:"))
if n%3==0 and n%7==0 :
    print("divisible by both 3 and 7")
elif n%3==0:
    print("divisible only by 3")
elif n%7==0:
    print("divisible only by 7")
else :
    print("divisible by none")
