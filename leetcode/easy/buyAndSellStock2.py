class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit  = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxProfit+=prices[i]-prices[i-1]
        return maxProfit
                
