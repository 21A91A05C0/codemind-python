n=int(input())
arr=list(map(int,input().split()))
m=int(input())
brr=list(map(int,input().split()))
k=[]
for i in range(len(brr)):
    k.insert(brr[i],arr[i])
print(*k)
    