class Solution(object):
    def findPairs(self, nums, k):

        count=0
        list_nums = set(nums)
        if k == 0:
            for each in list_nums:
                if nums.count(each)>1:
                    count+=1
            return count
        elif k < 0:
            return 0
        elif k > 0:
            for i in list_nums:
                if i+k in list_nums:
                    count+=1
        return count
