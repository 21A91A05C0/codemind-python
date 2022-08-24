n=int(input())
arr=list(map(int,input().split()))
k=[]
c=0
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if(i!=j and arr[i]==arr[j]):
            c=c+1
    if(c==1):
        continue
    else:
        k.append(arr[i])
print(*k)