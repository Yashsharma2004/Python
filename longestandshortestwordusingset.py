#Write  a python program to find the longest and shortest word in a given string.(using set)

str=input("enter a string:")
l=set(str.split())
long=len(max(l,key=len))
short=len(min(l,key=len))
print('longest words:')
for i in l:
        if len(i)==long:
            print(i)
print('shortest word:')
for i in l :
        if len(i)==short:
            print(i)
        
            
        




