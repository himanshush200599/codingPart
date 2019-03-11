# optimized solution by someone
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        nums[position:] = [0] * (len(nums)-position)

# my solution by removing zeros
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                s = nums.pop(nums.index(i))
                nums.append(s)
            
