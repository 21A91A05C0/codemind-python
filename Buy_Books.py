t=int(input())

m=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
s1=0
for i in m:
    s=s+i
for i in l:
    s1=s1+i
if(s-s1<0):
    print(abs(s-s1))
else:
    print("0")