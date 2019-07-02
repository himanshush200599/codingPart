# space complexity - O(d) and time complexity - O(N)
# where d id depth of tree for recursive calls
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self,root):
        return self.validateBSTHelper(root,float("-inf"),float("inf"))

    def validateBSTHelper(self,root,mini,maxi):
        if root is None:
            return True
        if root.val < mini or root.val >=maxi:
            return False
        IsLeftValid = self.validateBSTHelper(root.left,mini,root.val)
        return IsLeftValid and self.validateBSTHelper(root.right,root.val+1,maxi)
