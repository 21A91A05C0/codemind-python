n=int(input())
k=[]
arr=list(map(int,input().split()))
for i in range(0,len(arr),2):
    while(arr[i]>0):
        k.append(arr[i+1])
        arr[i]=arr[i]-1
print(*k)