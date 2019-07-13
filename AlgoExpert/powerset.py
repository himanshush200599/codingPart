def powerset(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            currentSubsets = subsets[i]
            subsets.append(currentSubsets+[num])
    return subsets
