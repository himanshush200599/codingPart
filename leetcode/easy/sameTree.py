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




#2nd method without inorder traversal
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
