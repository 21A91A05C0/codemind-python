s=input()
c=1
ma=1
for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
        c=c+1
        if(ma<c):
            ma=c
    else:
        c=1
print(ma)