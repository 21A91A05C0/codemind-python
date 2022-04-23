t=int(input())
while(t>0):
    n=int(input())
    i=1
    flag=0
    for i in range(1,n+1):
        if(n==i*i):
            flag=1
    if(flag==0):
        print("False")
    else:
        print("True")
            
    t=t-1