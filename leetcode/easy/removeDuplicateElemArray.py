class Solution:
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        j= 0
        n = len(arr)
        if n==0:
            return 0
        for i in range(0, n-1):
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1

        arr[j] = arr[n-1]
        j += 1
        return arr[:j+1]
