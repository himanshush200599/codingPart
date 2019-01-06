# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        if self.hasPathSum(root.left,sum = sum-root.val):
            return True
        if self.hasPathSum(root.right,sum-root.val):
            return True
        return False
