n=int(input())
a1=list(map(int,input().split()))
o=[]
e=[]
for i in a1:
    if(i%2!=0):
        o.append(i)
    else:
        e.append(i)
i=0
j=0
while((i<len(e)) or (j<len(o))):
    if(i<len(e)):
        print(e[i],end=" ")
        i=i+1
    if(j<len(o)):
        print(o[j],end=" ")
        j=j+1
if(n%2!=0):
    print(0)