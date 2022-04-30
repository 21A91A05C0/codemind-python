num1,num2=map(int,input().split())
lcm=0
gcd=0
for i in range(1,num1+1) and range(1,num2+1):
    if(num1%i==0 and num2%i==0):
        gcd=i
lcm=(num1*num2)/gcd
print("%d"%lcm)
