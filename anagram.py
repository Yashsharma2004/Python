#write a python program to check two given strings are anagram or not
s1=input('enter string:').lower()
s2=input('enter string:').lower()
if (sorted(s1)==sorted(s2)):
    print("given strings are anagram")
else:
    print("given strings are not anagram")    