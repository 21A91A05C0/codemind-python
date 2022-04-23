t=int(input())
while(t>0):
    n=int(input())
    f=1
    i=1
    for i in range(1,n+1):
        f=f*i
    print(f)
    t=t-1