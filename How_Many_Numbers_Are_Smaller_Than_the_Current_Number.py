n=int(input())
m=list(map(int,input().split()))
for i in range(len(m)):
    a=m[i]
    c=0
    for j in range(len(m)):
        if(m[j]<a):
            c=c+1
    print(c,end=" ")