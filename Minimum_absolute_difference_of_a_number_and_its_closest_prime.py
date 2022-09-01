def prime(n):
    c=0
    if(n==1):
        return 0
    else:
        for i in range(1,n+1):
            if(n%i==0):
                c=c+1
        if(c==2):
            return 1
    return 0
n=int(input())
#print(n)
k=[]
for i in range(n-10,n+10):
    if(prime(i)):
        k.append(i)
z=[]
x=[]
for i in range(len(k)):
    if(k[i]<n):
        z.append(k[i])
    else:
        x.append(k[i])
q=z[-1]   
w=x[0]
if(n-q<w-n):
    print(n-q)
else:
    print(w-n)
#print(q,w)
#print(x)
#print(z)