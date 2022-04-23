n=int(input())
res=n*n
sum=0
while(res>0):
    d=res%10
    sum=sum+d
    res=res//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")