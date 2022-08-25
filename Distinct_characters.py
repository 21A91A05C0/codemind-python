n=input().lower()
l=""
for i in n:
    if(n.count(i)==1):
        l=l+i
l=list(l)
l.sort()
l=str(l)
l=l.replace(" ","")
l=l.replace(",","")
l=l.replace("[","")
l=l.replace("]","")
l=l.replace("'","")


print(l)