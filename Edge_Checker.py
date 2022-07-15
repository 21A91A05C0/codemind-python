n,m=list(map(int,input().split()))
if(n-m==1 or m-n==1):
    print("Yes")
elif((n==10 and m==1) or (m==10 and n==1)):
    print("Yes")
else:
    print("No")