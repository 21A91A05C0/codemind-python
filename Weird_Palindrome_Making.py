t=int(input())
while(t>0):
    l=int(input())
    k=list(map(int,input().split()))
    c=0
    for i in k:
        if(i%2!=0):
            c=c+1
    print(c//2)        
    t=t-1