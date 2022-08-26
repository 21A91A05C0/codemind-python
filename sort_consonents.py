n=input().split(" ")
t=[]
for i in n:
    v=""
    c=""
    l=""
    for j in i:
        if j in "AEIOUaeiou":
            v=v+j
        elif j!=" ":
            c=c+j
    c=sorted(c)
    k=0
    p=0
    for j in i:
        if j in "AEIOUaeiou":
            l=l+v[k]
            k=k+1
        elif j!=" ":
            l=l+c[p]
            p=p+1
    t.append(l)
print(*t)