n=int(input())
arr=list(map(int,input().split()))
k=sum(arr)
while(n):
    if(k%n==0):
        print(n)
        break
    else:
        n=n-1