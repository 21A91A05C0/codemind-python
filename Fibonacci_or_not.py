n=int(input())
f1=0
f2=1
f3=f1+f2
while(f3<n):
    f1=f2
    f2=f3
    f3=f1+f2
if(f3==n):
    print("True")
else:
    print("False")