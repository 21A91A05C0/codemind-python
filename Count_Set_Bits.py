t=int(input())
while(t>0):
    n=int(input())
    c=0
    while(n):
        c=c+(n&1)
        n>>=1
    print(c)
    t=t-1