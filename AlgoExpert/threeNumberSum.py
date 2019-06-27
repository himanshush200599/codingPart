def threeNumberSum(array,target):
    res = []
    n = len(array)
    array.sort()
    for i in range(n-2):
        left = i+1
        right = n-1
        while left<right:
            currSum = array[i]+array[left]+array[right]
            if currSum==target:
                res.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif currSum<target:
                left = left+1
            else:
                right= right-1
    return res

print(threeNumberSum([1,2,3,1,5,4],6))
