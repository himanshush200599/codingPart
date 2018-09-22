class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        return False
 """
solution without converting into string in -
Time complexity : O(logn)

Space complexity : O(1).
 """
 class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        remainder = 0
        if ((x<0) or (x%10==0 and x!=0)):
           return False
        revertedNumber = 0
        while x>revertedNumber:
            remainder = x%10
            revertedNumber = revertedNumber*10 + remainder
            x = x//10
        if x==revertedNumber or x == revertedNumber//10:
            return True
        else:
            return False
a = Solution()
print(a.isPalindrome(123))
