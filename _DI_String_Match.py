n=input()
k=[]
s=len(n)
o=0
for i in range(0,len(n)):
    if(n[i]=='I'):
        k.append(o)
        o=o+1
    else:
        k.append(s)
        s=s-1
print(*k,end=' ')
print(o)
    