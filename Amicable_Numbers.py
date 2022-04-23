n=int(input())
m=int(input())
i=1
j=1
sum=0
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
for j in range(1,m):
    if(m%j==0):
        sum1=sum1+j
if(sum==m  and sum1==n):
    print("Amicable")
else:
    print("Not Amicable")