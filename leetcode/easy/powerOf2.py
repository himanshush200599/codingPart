class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1 or n==2:
            return True
        if n ==0:
            return False
        while n%2==0:
            n = int(n/2)

        if n==1:
            return True
        else:
            return False
