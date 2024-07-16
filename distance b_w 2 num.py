#write a python program to take x and y coordinates of two points and print distance between them.
x1=int(input('Enter value of x1 :'))
x2=int(input('Enter value of x2 :'))
y1=int(input('Enter value of y1 :'))
y2=int(input('Enter value of y2 :'))
dis= ((x1-x2)**2+(y1-y2)**2)**0.5
print(f'distance between x and y coordinate is {dis}')
