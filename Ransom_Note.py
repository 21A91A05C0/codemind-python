n,m=map(str,input().split())
m=list(m)
c=0
for i in n:
    if i in m:
        c=c+1
        m.remove(i)
if(c==len(n)):
    print("True")
else:
    print("False")