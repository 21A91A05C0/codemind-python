n,w=map(int,input().split())
i=1
for i in range(1,w+1):
    if(i%2==0):
        continue
    else:
        print("%d x %d = %d"%(n,i,n*i));