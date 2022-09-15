s=input()
s1=''
for i in s:
    if(i==' '):
        continue
    else:
        s1=s1+i
print(min(s1),s1.count(min(s1)),max(s1),s1.count(max(s1)))