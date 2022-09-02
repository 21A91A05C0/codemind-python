n=input().lower().split(" ")
c=0
v="aeiou"
for i in n:
    k=0
    j=len(i)-1
    while(k<j):
        if((i[k] in v and i[j] not in v) or (i[j] in v and i[k] not in v)):
            c=c+1
        k=k+1
        j=j-1
print(c)