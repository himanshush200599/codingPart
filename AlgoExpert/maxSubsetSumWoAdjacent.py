# Time Complexity  - O(N)
# Space Complexity - O(N)

def maxSubsetSumWoAdjacent(arr):
    if len(arr)==0:
        return -1
    if len(arr)==1:
        return arr[0]
    if len(arr)==2:
        return max(arr)
    maxSums = arr[:]
    # maxSums[0] = arr[0]
    maxSums[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        maxSums[i] = max(maxSums[i-1],maxSums[i-2]+arr[i])
    return maxSums[-1]


# Time Complexity  - O(N)
# Space Complexity - O(1)

def maxSubsetSumWoAdjacent(arr):
    if len(arr)==0:
            return 0
        if len(arr)==1:
            return arr[0]
        if len(arr)==2:
            return max(arr)
        # maxSums[0] = arr[0]
        first = arr[0]
        second = max(first , arr[1])
        for i in range(2,len(arr)):
            current = max(second,first+arr[i])
            first =second
            second = current
        return second
