n,x=map(int,input().split())
arr=list(map(int,input().split()))
s=l=0
for i in range(n):
    if(arr[i]<=x):
        s=s+1
    elif(arr[i]>x):
        
        if(l==1):
            break
        else:
            l=l+1
            continue
print(s)