s=input()
u=s.count('U')
d=s.count('D')
l=s.count('L')
r=s.count('R')
if(r==l and u==d):
    print('True')
else:
    print('False')