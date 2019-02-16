class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False
