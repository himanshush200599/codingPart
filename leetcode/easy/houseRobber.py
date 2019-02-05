class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        inc = nums[0]
        exc = 0
        for i in range(1,len(nums)):
            temp = inc
            inc = max(inc,exc+nums[i])
            exc = temp
        return inc
