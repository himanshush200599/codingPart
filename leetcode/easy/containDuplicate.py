from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = defaultdict(int)

        for i in nums:
            if d[i]>0:
                return True

            d[i]+=1
        else:
            return  False
            
