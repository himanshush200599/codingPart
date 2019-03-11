class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        if num%9==0:
            return 9

        for i in range(10):
            if (num-i)%9==0:
                return i
# my solution
# based on article of wikipedia
# self generated
# concept - 
# when answer is subtracted from actual  number then number becomes multiple of 9
