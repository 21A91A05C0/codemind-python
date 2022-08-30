from itertools import permutations
n,m=map(int,input().split())
s=''
k=[]
for i in range(1,n+1):
    s=s+str(i)
for p in permutations(s):
    k.append(p)
for i in range(0,len(k)):
    if i==m-1:
        print("".join(k[i]))

    