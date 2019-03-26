class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in set(t):
            if t.count(c) > s.count(c):
                return c
