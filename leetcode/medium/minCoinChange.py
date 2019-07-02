class Solution(object):
    def coinChange(self, coins, n):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minCoins = [float("inf") for _ in range(n+1)]
        minCoins[0] = 0
        for coin in coins:
            for amount in range(1,n+1):
                if coin<=amount:
                    minCoins[amount] = min(minCoins[amount],1+minCoins[amount-coin])
        return minCoins[n] if minCoins[n]!=float("inf") else -1
