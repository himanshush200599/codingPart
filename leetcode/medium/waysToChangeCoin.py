class Solution(object):
    def change(self, n, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        ways = [0  for i in range(n+1)]
        ways[0] = 1
        for coin in coins:
            for amount in range(1,n+1):
                if coin<=amount:
                    ways[amount]+=ways[amount-coin]
        return ways[n]
