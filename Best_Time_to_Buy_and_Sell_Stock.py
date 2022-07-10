n=int(input())
prices=list(map(int,input().split()))

buy=0
sell=1
maxx=0
while(sell<len(prices)):
    if(prices[buy]<prices[sell]):
        price=prices[sell]-prices[buy]
        maxx=max(maxx,price)
    else:
        buy=sell
    sell=sell+1
print(maxx)