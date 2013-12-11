# l: coin value, n: total sum
def numberOfWays(coins,total):
    if len(coins)==1:
        return 1
    else:
        res=0
        coinsPopped=coins[:]
        last = coinsPopped.pop()
        # i number of last coins used
        for i in range(0,total/last + 1):
            res+= numberOfWays(coinsPopped,total-i*last)
        return res

print numberOfWays([1,2,5,10,20,50,100,200],200)
    
