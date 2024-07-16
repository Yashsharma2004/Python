# write a python program to find the amount of each installment by taking principal , rate  and time from user.
# formula for monthly EMI is --> p*r*(1+r)**n/((1+r)**n-1)
P=float(input('Enter principal amount :'))
R=float(input('Enter interest rate :'))
n=float(input('Enter no . of months :'))
r=R/(12*100)
EMI=P*r*(1+r)**n/((1+r)**n-1)
print(f"Monthly EMI is  {EMI}")
