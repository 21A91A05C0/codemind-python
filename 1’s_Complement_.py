n=int(input())
k=bin(n)[2:]
k=str(k)
m=''
for i in range(len(k)):
    if(k[i]=='1'):
        m=m+'0'
    else:
        m=m+'1'
print(int(m,2))