"""
Implementation of  binary searh tree in python.
Basic principle -
    for all  nodes x, if  y is in the left subtree of x then
    key(y) <= key(x)
    reverse for right.
"""
class Node:
    def __init__(self,value):
        self.data  = value
        self.right = None
        self.left = None
        self.parent = None
class BST:
    def __init__(self):
        self.root = None
    def inorderTraversal(self,root):

        if root is not None:
            self.inorderTraversal(root.left)
            print(root.data,end = ' ')
            self.inorderTraversal(root.right)

    def preorderTraversal(self,root):
        if root is not None:
            print(root.data , end=' ')
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
    def postorderTraversal(self,root):
        if root is not None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.data , end=' ')
    def searching(self,root,key):
        if root is None or root.data == key:
            return root
        if key >= root.data:
            return searching(root.right,key)
        else:
            return searching(root.left,key)
    def minimum(self,root):
        while root.left is not None:
            root = root.left
        return root
    def maximum(self,root):
        while root.right is not None:
            root = root.right
        return root
    def treeSuccessor(self,root):
        if root.right is not None:
            return self.minimum(root.right)
        y  = root.parent
        while y is not None and root == y.right:
            root = y
            y = y.parent
        return y
    def TreePredecessor(self,root):
        if root.left is not None:
            return self.maximum(root)

        y = root.parent
        while (y is not None and root == y.right):
            root = y
            y = y.parent
        return y

    def insertion(self, data ):
        if self.root is None:
            self.root  = Node(data)
        else:
            self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = Node(data)


    #def transplant(self,u,v):
        #""" replace node v with node u"""
        #if u.parent is None:
            #self.root  = v
        #elif u == u.parent.left:
        #    u.parent.left = v
        #else:
        #    u.parent.right = v
        #if v is not None:
        #    v.parent  = u.parent
    def removeNode(self,node,data):
        """ first 3 are to find node to be deleted """
        if not node:
            return node
        if node.data < data:
            node.right = self.removeNode(node.right,data)
        elif node.data > data:
            node.left = self.removeNode(node.left,data)

        else:
            if  node.left is None and node.right is None:
                print("Here we are deleting a leaf node , thus deleted daata is ",node,data)
                del node
                return None
            elif node.left is None:
                print(" deleting a node which has only right child and data is ",node.data)
                node.data  = node.right.data
                node = node.right
                del node
                return None
            elif node.right is  None:
                print("deleting node has only left child and data is ",node.data)
                node.data = node.left.data
                node = node.left
                del node
                return None
            else:
                tempNode = self.TreePredecessor(node)
                node.data = tempNode.data
                node.left  = self.removeNode(node.left,tempNode.data)



a = BST()
elements = [2,4,7,6,5,9,17,1]
for i in elements:
    a.insertion(i)
print("Inorder traversing of binary search tree --")
a.inorderTraversal(a.root)
print()
print("Preorder traversing of BST")
a.preorderTraversal(a.root)
print()
print("Postorder traversing of BST")
a.postorderTraversal(a.root)
print()
print("minimum elements is -")
print(a.minimum(a.root).data)
print("maximum elements is ")
print(a.maximum(a.root).data)

print("treeSuccessor is -")
print(a.treeSuccessor(a.root).data)
print("TreePredecessor is -")
print(a.TreePredecessor(a.root).data)
print("root of the tree is -")
print(a.root.data)
print("deleting node from BST")

a.removeNode(a.root,2)
print("root of the tree is -")
print(a.root.data)
