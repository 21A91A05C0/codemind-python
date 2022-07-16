s1=input()
s2=input()
a1=" "
b2=" "
arr=[]
for i in s1:
    if i.isspace():
        continue
    else:
        a1=a1+i.lower()
    
for i in s2:
    if i.isspace():
        continue
    else:
        b2=b2+i.lower()
for i in a1:
    if i not in b2:
        if i not in arr:
            arr.append(i)
for i in b2:
    if i not in a1:
        if i not in arr:
            arr.append(i)
arr.sort()
print("".join(arr))