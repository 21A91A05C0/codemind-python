n=input().split(" ")
k=[]
v='aeiouAEIOU'
l=[]
for i in range(len(n)):
    k.append(n[i])
for i in range(len(k)):
    if(k[i][0] in v):
        k[i]=k[i]+'ma'+(i*'a')+'a'
        print(k[i],end=" ")
    else:
        k[i]=k[i][1:]+k[i][0]+'ma'+(i*'a')+'a'
        print(k[i],end=" ")