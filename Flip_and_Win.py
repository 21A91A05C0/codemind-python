n=int(input())
s=input()
sum=0
for i in range(1,len(s)):
    sum=sum+abs(int(s[i])-int(s[i-1]))
#print(sum)
d=n-sum-1
#print(d)
if((d%3)==0):
    print('Sudhir')
else:
    print('Ashok')
    