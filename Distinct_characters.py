s=input().lower()
s=set(s)
k=sorted(s)
l=''
for i in k:
    if(i==' '):
        continue
    else:
        l=l+i
print(l)