t=int(input())
while(t>0):
    n=int(input())
    #print(n)
    k=[]
    flag=0
    while(n!=0):
        d=n%10
        #print('hi')
        k.append(d)
        n=n//10
    #print(k)
    m=max(k)
    l=min(k)
    for i in range(l,m+1):
        if i not in k:
            flag=1
            
    if(flag==1):
        print('NO')
    else:
        print('YES')

    
    t=t-1