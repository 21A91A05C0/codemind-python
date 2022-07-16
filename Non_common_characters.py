s1=input()
s2=input()
a1=""
b1=""
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
        b1=b1+i.lower()
for i in a1:
    if i not in b1:
        if i not in arr:
            arr.append(i)
for i in b1:
    if i not in a1:
        if i not in arr:
            arr.append(i)
print(len(arr))