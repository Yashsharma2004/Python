#write a program to count number of vowels,consonants,space,speacial cahracters,spaces,upper case alphabets,lower case alphabets,words in a given string.

inp=input('enter:')
st='aeiouAEIOU'
v=0
c=0
d=0
sp=0
uc=0
lc=0
s=0
for i in inp:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        if i in st:
            v+=1
        else:
            c+=1
        if ord(i)>=65 and ord(i)<=90:
            uc+=1
        if ord(i)>=97 and ord(i)<=122:
                lc+=1
    elif ord(i)>=48 and ord(i)<=57:
                d+=1
    elif i==' ':
            s+=1
    else:
            sp+=1
print(f' vowels={v}\n consonants={c}\n upper case={uc}\n lower case ={lc}\n digit={d}\n space={s}\n special characters={sp}\n words={s+1}')                        