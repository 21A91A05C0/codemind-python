s=input()
t=input()
o=[]
p=[]
for i in s:
    if(i=='#'):
        o.pop()
    else:
        o.append(i)
for i in t:
    if(i=='#'):
        p.pop()
    else:
        p.append(i)
if(p==o):
    print('True')
else:
    print('False')