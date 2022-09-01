def palin(n):
    z=n
    r=0
    while(n):
        d=n%10
        r=r*10+d
        n=n//10
    if(r==z):
        return 1
    else:
        return 0
n=int(input())
#print(n)
k=0
l=0
for i in range(n-10,n):
    if(palin(i)):
        k=i
        
for i in range(n+1,n+11):
    if(palin(i)):
        l=i
if(abs(k-n)<abs(n-l)):
    print(k)
elif(abs(k-n)==abs(n-l)):
    print(k,l)
else:
    print(l)