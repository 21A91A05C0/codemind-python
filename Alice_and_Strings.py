t=int(input())
while(t>0):
    s=input()
    d=input()
    for i in range(len(s)):
        if(ord(s[i])>ord(d[i])):
            print('NO')
            break
    else:
        print('YES')
    t=t-1