n=int(input())
sq=n*n
temp=n
c=0
while(n>0):
    d=n%10
    n=n//10
    c=c+1
n=temp
pw=10**c
k=sq%pw;
if(n==k):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")