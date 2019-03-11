class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumOfListOfNNaturalNumber =( n*(n+1))/2
        return sumOfListOfNNaturalNumber-sum(nums)
