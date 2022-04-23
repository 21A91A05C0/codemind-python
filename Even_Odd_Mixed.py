n=int(input())
c=0
k=0
z=0
p=n
while(n>0):
    d=n%10
    if(d%2==0):
        c=c+1
        
    elif(d%2!=0):
        k=k+1
    z=z+1
    n=n//10

if(c==z):
    print("Even")
elif(k==z):
    print("Odd")
else:
    print("Mixed")
    