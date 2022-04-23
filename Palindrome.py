t=int(input())
n=0
rev=0
n=t
while(t>0):
    d=t%10
    rev=rev*10+d
    t=t//10
if(n==rev):
    print("True")
else:
    print("False")
    