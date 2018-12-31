class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s)==0:
            return 0
        if len(s) == 1:
            return 1
        s = s.split()
        return len(s[-1])
