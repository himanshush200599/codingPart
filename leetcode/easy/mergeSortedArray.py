class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        lastIndex = n+m-1
        while  j>=0:
            if  i>=0 and nums1[i]>nums2[j]:
                nums1[lastIndex] = nums1[i]
                i-=1
            else:
                nums1[lastIndex] = nums2[j]
                j-=1
            lastIndex-=1
