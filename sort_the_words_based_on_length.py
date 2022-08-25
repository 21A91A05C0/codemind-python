l=list(map(str,input().split()))
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if(i!=j and len(l[i])<len(l[j])):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(*l)