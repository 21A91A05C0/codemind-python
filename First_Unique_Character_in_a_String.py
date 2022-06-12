s=input().lower()
k=[]
flag=0
for i in range(len(s)):
    flag=0
    for j in range(len(s)):
        if s[i]==s[j] and i!=j:
            flag=1
            break
    else:
        k.append(i)
        print(*k)
        break
if(flag==1):
    print(-1)