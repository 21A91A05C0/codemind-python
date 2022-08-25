n=input().lower()
v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
i=0
d=0
j=len(n)-1
while(i<j):
    if((n[i] in v and n[j] in c) or (n[i] in c and n[j] in v)):

        d=d+1
    i=i+1
    j=j-1
print(d)
