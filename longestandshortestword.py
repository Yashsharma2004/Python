#Write  a python program to find the longest and shortest word in a given string.

str=input("enter a string:")
l=str.split()
long=len(max(l,key=len))
short=len(min(l,key=len))
ll=[]
ls=[]
print('longest words:')
for i in l:
    if i not in ll:
        if len(i)==long:
            print(i)
            ll.append(i)
print('shortest word:')
for i in l :
    if i not in ls:
        if len(i)==short:
            print(i)
            ls.append(i)
            