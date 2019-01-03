class Tree(object):
    """docstring for Tree."""
    def __init__(self, val):
        super(Tree, self).__init__()
        self.left = None
        self.right = None
        self.val = val
class Solution(object):
    def isSymmetric(self,root):
        """
            We have to compare left and right tree whether they are mirror image of each other or not
        """
        def isMirror(root1,root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                if root1.val == root2.val:
                    return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
            return False
        return isMirror(root,root)
