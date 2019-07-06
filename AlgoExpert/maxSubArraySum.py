# Kadane's Algorithms using O(N)

def maxSubArraySum(arr):
    n = len(arr)
    currMax = 0
    maxi = 0
    for num in arr:
        currMax = max(currMax+num,num)
        maxi = max(maxi,currMax)
    return maxi
print(maxSubArraySum([3,-2,4]))
