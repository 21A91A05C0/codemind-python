t=int(input())
while(t>0):
    n=int(input())
    me=list(map(int,input().split()))
    fr=list(map(int,input().split()))
    k=[]
    for i in me[1:]:
        if i not in k:
            k.append(i)
    for i in fr[1:]:
        if i not in k:
            k.append(i)
    #z=set(k)
    #print(n)
    #print(set(k))
    if(len(k)==n):
        print('YES')
    else:
        print('NO')
    
    
    t=t-1