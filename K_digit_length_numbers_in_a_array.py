a,b=map(int,input().split())
l=list(map(int,input().split()))
k=[]
c=0
for i in range(len(l)):
    if(l[i]<0):
        k.append(len(str(l[i]))-1)
        
    else:
        k.append(len(str(l[i])))
for i in range(len(k)):
    if(k[i]==b):
        c=c+1
print(c)