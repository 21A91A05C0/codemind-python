n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
o=[]
z=[]
while(q):
    l=int(input())
    o.append(l)
    q=q-1
#print(o)
for i in range(len(arr)):
    z.append(arr[(n-k+i)%n])
#print(z)
h=[]
for i in range(len(o)):
    print(z[o[i]])
            
    
    
    