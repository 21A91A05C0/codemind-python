n=int(input())
l=list(map(int,input().split()))
m=n//2
k=[]
for i in range(m):
    k.append(l[i])
    k.append(l[i+m])
print(*k)
    
