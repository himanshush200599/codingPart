# Incrementing all but one is equivalent to decrementing that one.
# So let's do that instead. How many single-element decrements to make all equal?
# No point to decrementing below the current minimum, so how many single-element decrements to
# make all equal to the current minimum? Just take the difference from what we currently
# have (the sum) to what we want (n times the minimum).
# from leetcode discussion   
def minMoves(self, nums):
    return sum(nums) - len(nums) * min(nums)
