def isprime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        if(isprime(i)==1 and isprime(j)==1):
            if(i*j==n):
                print(i,j)
                c=1
                break
    if(c==1):
        break
if(c==0):
    print(-1)
            