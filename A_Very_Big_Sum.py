n=int(input())
sum=0
v=list(map(int,input().split()))
for i in range(len(v)):
    sum=sum+v[i]
print(sum)