class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = prices[:]
        minPrice = 9999
        profit  = 0
        for item in l:
            if item<minPrice:
                minPrice = item
            elif item-minPrice >profit:
                profit = item-minPrice
        return profit
    
