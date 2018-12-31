class Solution:
    def maxSubArray(self, l):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        p = min(l)
        for i in range(len(l)):
            s = max(l[i],s+l[i])
            p = max(s,p)
        return p
