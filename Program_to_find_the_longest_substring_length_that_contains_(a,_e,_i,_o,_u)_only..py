s=input()
c=0
ma=0
v='aeiou'
for i in range(len(s)):
    if(s[i] in v):
        c=c+1
        if(ma<c):
            ma=c
    else:
        c=0
print(ma)