n=input()
k=[]
c=0
c1=0
for i in n:
    k.append(n.count(i))
ma=max(k)
mn=min(k)
for i in n:
    if n.count(i)==ma:
        c=c+1
    elif(n.count(i)==mn):
        c1=c1+1
if c==len(n) or c1==len(n) or c==len(n)-1 or c1==len(n)-1:
    print('Valid String')
else:
    print('Not Valid')
    