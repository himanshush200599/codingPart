class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = 0
        for i in nums:
            d[i] +=1
        for key,value in d.items():
            if value == 1:
                return key
        
