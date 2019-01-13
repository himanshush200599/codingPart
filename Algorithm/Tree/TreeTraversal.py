class TreeNode(object):
    """docstring for TreeNode."""
    def __init__(self, val):
        super(TreeNode, self).__init__()
        self.val = val
        self.left = None
        self.right = None
class Traversal(object):
    def inorder(self,root):
        if root is None:
            return
        st = []
        while root is not None or len(st)>0:
            if root is not None:
                st.append(root)
                root = root.left
            else:
                root = st.pop(-1)
                print(root.val,end=' ')
                root = root.right
        print()
    def preorder(self,root):
        if root is None:
            return
        st = []
        while root is not None or len(st)>0:
            if root is not None:
                print(root.val,end=' ')
                st.append(root)
                root = root.left
            else:
                root = st.pop(-1)
                root = root.right
        print()
    def postorder(self,root):
        if root is None:
            return
        st = []
        st2 = []
        while root is not None or len(st)>0:
            if root is not None:
                st2.append(root.val)
                st.append(root)
                root = root.right
            else:
                root = st.pop(-1)
                root = root.left
        print(st2[::-1])
a = TreeNode(1)
a.left = TreeNode(3)
a.left.left = TreeNode(6)
a.left.right = TreeNode(7)
a.right = TreeNode(5)
b = Traversal()
b.inorder(a)
b.preorder(a)
b.postorder(a)
