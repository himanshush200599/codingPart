class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i=5
        while (n/i>=1):
            count += int(n/i)
            i *= 5

        return int(count)
#code from geeksforgeeks
#explanation is awesome
