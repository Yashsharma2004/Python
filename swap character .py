#Write a Python program to swap all the characters in a given string from lower case to upper case and upper case to lower case. (Don’t use any string built-in methods)
#(Hint: pyTHon<->PYthON)


str=input()
e=""
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        e=e+chr(ord(i)+32)
    elif ord(i)>=97 and ord(i)<=122:
        e=e+chr(ord(i)-32)
    else:
        e=e+i
print(e)