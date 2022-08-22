n,m=map(int,input().split())
if(n==1 and m==10):
    print("Yes")
elif(m==1 and n==10):
    print("Yes")
elif(n-m==1):
    print("Yes")
elif(m-n==1):
    print("Yes")
else:
    print("No")
