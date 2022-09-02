s=input().lower()
v='aeiou'
c='qwrtypsdfghjklzxcvbnm'
i=0
j=len(s)-1
z=0
while(i<j):
    if((s[i] in v) and (s[j]  in c)or (s[i] in c) and (s[j] in v)):
        z=z+1
    i=i+1
    j=j-1
    
print(z)