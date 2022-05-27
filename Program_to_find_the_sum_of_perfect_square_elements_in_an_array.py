n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    for j in range(1,10):
        if(arr[i]==j**2):
            sum=sum+arr[i]
print(sum)