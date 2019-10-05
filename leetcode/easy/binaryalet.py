class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=bin(n).replace("0b","")
        for i in range(len(x)-1):
            if x[i]==x[i+1]:
                return False
        return True
            
