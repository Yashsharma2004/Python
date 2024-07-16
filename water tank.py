# Given a water tank(cylindrical shape) with height=10m and radius=5m. consider a water pump having flow rate of 15m^3/min. now your task is to write a python program where user can enter the time for the pump to be ON and find the status of tank that can be underflow,overflow or full with the water at given time for pump to be on. also display the filled height and remaining height of the tank if tank status is underflow.


h=10
r=5
f=15
t=float(input('enter the time for pump:'))
vtank=3.14*r**2*h
vwtr=f*t
if vwtr<vtank:
    print('underflow condition')
    ht=vwtr/(3.14*r**2)
    hr=h-ht
    print(f'filled height: {ht}')
    print(f'remaining height: {hr}')
elif vwtr>vtank:
    print('overflow conditon')
    print('volume of',vwtr-vtank) 
else:
    print('tank full')       