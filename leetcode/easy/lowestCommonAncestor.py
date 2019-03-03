# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p1 = p.val
        q1 = q.val
        while root:
            r1 = root.val
            if p1>r1 and q1>r1:
                root = root.right
            elif p1<r1 and q1<r1:
                root = root.left
            else:
                return root
