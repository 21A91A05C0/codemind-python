n=int(input())
p=[]
h=[]
f=n
while(n>0):
    l=int(input())
    p.append(l)
    n=n-1
while(f>0):
    o=int(input())
    h.append(o)
    f=f-1

c=0
for i in p:
    for j in h:
        if(i<=j):
            h.remove(j)
        #print(h)
print(len(h))