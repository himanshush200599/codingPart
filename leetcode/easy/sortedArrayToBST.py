# # # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==2:
            root=TreeNode(nums[1])
            root.left=TreeNode(nums[0])
            return root
        else:
            mid  = int(len(nums)/2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
