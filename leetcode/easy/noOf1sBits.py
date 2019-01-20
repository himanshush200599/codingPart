class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        c = 0
        for i in n:
            if i=='1':
                c+=1
        return c
