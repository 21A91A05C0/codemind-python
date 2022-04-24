n=int(input())
flag=0
for i in range(n):
    if(n==i*i):
        flag=1
if(flag==1):
    print("True")
else:
    print("False")