# # Dp solution from one of editor on Leetcode
# Basically here pattern is analyse
# like for n = 1 ans is 1
# for n=2 either we have 1   or 2 so ans is 2
#                         \     /
#                         2    1
# res[n] = res[0]*res[n-1] + res[1]*res[n-2] + res[2]*res[n-3] + ... + res[n-2]*res[1] + res[n-1]*res[0

# There is formula based on some calculations

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0]*(n+1)
        res[0] = 1
        for i in range(1,n+1) :
            for j in range(i) :
                res[i] += res[j]*res[i-1-j]
        return res[-1]
