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


# efficient way
return num>0 and num&(num-1)==0 and len(bin(num)[3:])%2==0
# from one of user on leetcode
