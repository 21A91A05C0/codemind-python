n=int(input())
arr=list(map(int,input().split()))
k=[]

for i in range(len(arr)):
    arr[i]=arr[i]*arr[i]
    k.append(arr[i])
s=sorted(k)
print(*s)