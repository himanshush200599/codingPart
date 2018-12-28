#my solution - Brute force
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <=nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(1,len(nums)):
            if target<=nums[i]:
                return i

#Optimal solution -  Binary search
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums)-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        left = 0
        right = len(nums)-1
        while left+1 < right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return left+1
        
