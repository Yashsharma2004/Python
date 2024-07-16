#write a program to count frequency of all characters in a given string.

st=input("enter string:")
r=' '
for i in st:
    if i not in r:
        print(f'{i}={st.count(i)}')
        
        r=r+i