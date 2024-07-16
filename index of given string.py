#write a python program to display all the index(or position) of the given pattern in a string(very important)

st='hello python program'
ch='o'
start=0
x=st.count(ch)
for i in range(x):
    re=st.index(ch,start)
    print(re,end=' ')
    start=re+1
