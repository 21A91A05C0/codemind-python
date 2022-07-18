a=input()
ma=0
c=0
v='aeiou'
for i in range(len(a)):
    c=0
    for j in range(i,len(a)):
        if a[j] in v:
            c=c+1
            if(ma<c):
                ma=c
        else:
            break
print(ma)
            