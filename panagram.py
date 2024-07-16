# write a python program to check given string is panagram or not.


str=input("Enter a string :")
str1=str.lower()
for i in range(97,123):
    c=chr(i)
    if c not in str1:
        print('Not panagram')
        break
else:
    print('Panagram')
  