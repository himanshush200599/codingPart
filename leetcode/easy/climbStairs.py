# this is extended version of fibonacci numbers 
# as for 1 stair -  1 way
# for 2 stair 2 ways -  1-1 and 2
# for 3 stairs theere are ways for 2 stairs and ways for 1 stairs
# formual = climbStairs(n-1)+climbStairs(n-1)
# 1 1 2 3 5 8 13 .......

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        """
        a = 1
        b = 0
        c=0
        if n==1 or n==2:
            return n
        for i in range(n):
            c = a+b
            b  = a
            a = c
        return c
