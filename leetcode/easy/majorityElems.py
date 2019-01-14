class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we can also used collections modules to count key and their counter
        n = len(nums)
        m = int(n/2)
        d = {}
        for i in nums:
            d[i] = 0
        for i in nums:
            d[i] +=1
        for key,value in d.items():
            if value > m:
                return key
