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
while((i<len(o)) or (j<len(e))):
    if(i<len(o)):
        print(o[i],end=" ")
        i=i+1
    if(j<len(e)):
        print(e[j],end=" ")
        j=j+1
if(n%2!=0):
    print(0)
