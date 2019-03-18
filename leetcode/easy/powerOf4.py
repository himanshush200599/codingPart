class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num%4==0 and num!=0:
            num/=4
        return num==1
    #Inefficient-gives  time limit exceeded
