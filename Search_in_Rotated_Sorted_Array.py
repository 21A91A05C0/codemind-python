n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(arr)):
    if(k==arr[i]):
        c=1
        print(i)
if(c==0):
    print(-1)