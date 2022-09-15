n=int(input())
#print(n)
a=0
b=1
k=[]
for i in range(1,n+1):
    k.append(a)
    c=a+b
    a=b
    b=c
l=[]
minn=999
p=0
for i in k:
    res=abs(i-n)
    l.append(res)
z=min(l)
o=[]
for i in range(len(l)):
    if(l[i]==z):
        o.append(k[i])
print(*o)
        
        
    