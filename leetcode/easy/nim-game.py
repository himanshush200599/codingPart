class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0

# Lemme explain this solution
# so lets we have only n stones
# i am starting from base case -
# if n = 1 - winner ME
# n = 2 = winner Me
# n = 3 winner Me
# thus it is clear that when number of stones left are less than 4 then winner will be ME
# Now  if n==4 then on any condition winner will be not me
# Thus whenever i have number which is divisible by 4
# then winner will be opponent
