#write a program to check given no. or string is palindrome or not
st=input("enter a string:")
out=st[::-1]
if st==out:
    print("palindrome") 
else:
    print("not palindrome")   