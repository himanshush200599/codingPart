class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                currentSubsets = subsets[i]
                subsets.append(currentSubsets+[num])
        return subsets
