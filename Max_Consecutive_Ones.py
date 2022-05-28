n=int(input())
arr=list(map(int,input().split()))
c=0
s=[]
for i in range(len(arr)):
    if(arr[i]==1):
        c=c+1
    else:
        s.append(c)
        c=0
s.append(c)
print(max(s))