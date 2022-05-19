n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
p=[]
p=sorted(set(arr1))
for i in  range(n):
    for j in range(len(p)):
        if(arr[i]==p[j] and arr[i]>0):
            print(arr[i],end=" ")
            p[j]=-1
            