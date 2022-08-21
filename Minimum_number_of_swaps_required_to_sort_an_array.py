n=int(input())
arr=list(map(int,input().split()))
cp=arr.copy()
cp.sort()
c=0
for i in range(n):
    if(arr[i]!=cp[i]):
        c=c+1
    ind=arr.index(cp[i])
    arr[i],arr[ind]=arr[ind],arr[i]
print(c)
    
    
    
