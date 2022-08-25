n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(len(arr)):
    maxx=-1
    for j in range(i+1,len(arr)):
        if(arr[j]>maxx):
            maxx=arr[j]
    k.append(maxx)
print(*k)
    
