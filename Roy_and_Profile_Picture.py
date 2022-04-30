l=int(input())
t=int(input())
while(t>0):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    else:
        if(w==h):
            print("ACCEPTED")
        else:
            print("CROP IT")
    t=t-1