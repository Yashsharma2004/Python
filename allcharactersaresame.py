#Write a python program to check if all characters in string are same or not. Print 'all characters are same' if all characters are same otherwise print None.

str=input("enter String:").lower()
length=len(str)
x=str[0]*length
if x==str:
    print("all characters are same")
else:
    print("None")