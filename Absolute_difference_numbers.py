n,m=map(int,input().split())
n=str(n)
k=''
for i in n:
    k=k+i
z=k[::-1]
l=k[:m]
p=z[:m]
p=p[::-1]
print(abs((int(l)-int(p))))
