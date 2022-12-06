n=int(input())
arr=list(map(int,input().split()))
k=set(arr)
m=[]
for i in k:
    if(arr.count(i)==1):
        m.append(i)
m=sorted(m)
print(*m)
    