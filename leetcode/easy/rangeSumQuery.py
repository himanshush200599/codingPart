#Inefficient solution using list comprehension
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1] )


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# efficint solution from leetcode
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cml = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.cml[i + 1] = self.cml[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cml[j + 1] - self.cml[i]
