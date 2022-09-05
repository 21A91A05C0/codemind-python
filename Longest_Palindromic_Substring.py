def fun(s):
    if(s==s[::-1]):
        return 1
    else:
        return 0
s=input()
k=''
l=[]
for i in range(len(s)):
    k=''
    for j in range(i,len(s)):
        k=k+s[j]
        #print(k)
        if(fun(k)):
            l.append(k)
z=set(l)
m=0
o=0
for i in z:
    if(len(i)>m):
        m=len(i)
        o=i
print(o)
        

    

    
    