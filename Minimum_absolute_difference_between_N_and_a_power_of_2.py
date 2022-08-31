from math import floor,log2
s=int(input())
l=pow(2,floor(log2(s)))
r=l*2
print(min((s-l),(r-s)))
