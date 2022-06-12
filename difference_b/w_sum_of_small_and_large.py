l=list(map(str,input().split()))
b=[]
k=[]
sum=0
sum1=0
for i in l:
    k.append(ord(min(i)))
    b.append(ord(max(i)))
for i in k:
    sum=sum+i
for j in b:
    sum1=sum1+j


z=abs(sum-sum1)    
print(z)