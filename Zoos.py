n=input()
y=0
X=0
i=0
for i in n:
    if(i=='z'):
        X=X+1
    else:
        y=y+1
if(y==2*X):
    print("Yes")
else:
    print("No")