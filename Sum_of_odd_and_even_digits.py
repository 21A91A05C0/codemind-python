n=int(input())
sum=0
sum1=0
res=0
p=list(map(int,input().split()))
for i in range(len(p)):
    if(i%2==0):
        sum=sum+p[i]
    else:
        sum1=sum1+p[i]
res=sum-sum1
if(res==0):
    print("YES")
else:
    print("NO")