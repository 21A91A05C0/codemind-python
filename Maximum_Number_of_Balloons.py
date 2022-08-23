p=input()
b=a=l=o=n=0
for i in p:
    if(i=='b'):
        b=b+1
    elif(i=="a"):
        a=a+1
    elif(i=="l"):
        l=l+1
    elif(i=="o"):
        o=o+1
    elif(i=="n"):
        n=n+1
ans=0
while(b>0 and a>0 and l>0 and o>0 and n>0):
    b=b-1
    a=a-1
    l=l-2
    if(l<0):
        break
    o=o-2
    if(o<0):
        break
    n=n-1
    ans=ans+1
print(ans)