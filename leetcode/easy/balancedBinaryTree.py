# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        def height(root):
            if not root:
                    return 0
            return 1 + max(height(root.left), height(root.right))
        lsub = height(root.left)
        rsub = height(root.right)
        if (abs(lsub - rsub) <= 1) and self.isBalanced(
    root.left) is True and self.isBalanced( root.right) is True:
            return True
        return False
