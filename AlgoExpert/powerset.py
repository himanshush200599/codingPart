# Time - O(2^n*n)
# Space - O(2^n*n)

def powerset(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            currentSubsets = subsets[i]
            subsets.append(currentSubsets+[num])
    return subsets
