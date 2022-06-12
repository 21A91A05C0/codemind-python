l=list(map(str,input().lower().split()))
l1=list(map(str,input().lower().split()))
c=0
for i in l:
    if i in l1:
        c=c+1
print(c)