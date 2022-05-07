n,m=map(int,input().split())
max=-9999
arr=[list(map(int,input().split()))for i in range (n)]
for j in range(m):
    max=-9999
    for i in range(n):
        if(max<arr[i][j]):
            max=arr[i][j]
    print(max)
        
        