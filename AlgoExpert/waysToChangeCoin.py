def waysChangeCoins(n,denoms): #n is amount given to  change using coins present in denoms
    ways = [0  for i in range(n+1)]
    ways[0] = 1
    for coin in denoms:
        for amount in range(1,n+1):
            if denom<=amount:
                ways[amount]+=ways[amount-coin]
    return ways[n]
