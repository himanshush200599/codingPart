class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = [2,3,5]
        if num<=0:
            return False
        for i in l:
            while num%i==0:
                num/=i

        return num==1
