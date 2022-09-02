t=int(input())
while(t>0):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    sum=0
    c=0
    for i in range(0,len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if(sum==m):
                c=c+1
                print(i+1,j+1)
            if(c>=1):
                break
    if(c==0):
        print(-1)
            
            
        
    t=t-1