n=input()
i=1
c=0
for i in n:
    if(i.isnumeric()):
        c=c+1
if(c>0):
    print("Contains %d digit"%c)
else:
    print("Doesn't contain digit")