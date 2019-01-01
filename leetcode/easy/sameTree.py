# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #here first we are calculating inorder traversal of both tree and thrn compare them
        def inorder(root,arr,child):
            if root:
                inorder(root.left,arr,"left")
                arr.append((root.val,child))
                inorder(root.right,arr,"right")
        arr1 = []
        inorder(p,arr1,"val")
        arr2 = []
        inorder(q,arr2,"val")
        return arr1==arr2
