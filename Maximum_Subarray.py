n=int(input())
arr=list(map(int,input().split()))
s=0
ma=-100
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+arr[j]
        if(s>ma):
            ma=s
print(ma)