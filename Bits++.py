t=int(input())
c=0
while(t>0):
    s=input()
    for i in range(len(s)):
        if(s[i]=="+"):
            c=c+1
            break
        elif(s[i]=='-'):
            c=c-1
            break
    
    t=t-1
print(c)