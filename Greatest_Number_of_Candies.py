n=int(input())
arr=list(map(int,input().split()))
m=int(input())
maxx=0
flag=0
for i in arr:
    if(maxx<i):
        maxx=i
for i in arr:
    if((i+m)>=maxx):
        print("True",end=" ")
    else:
        print('False',end=" ")

        
    