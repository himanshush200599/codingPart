"""
    Implementation of trees in pthon3|
    Trees are used when we have to store data in heirarchical order.
"""

#Node to be inserted in tree
#contain right and left pointer
class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

"""
Simple tree  using node.
"""
root  = Node(2)
root.left  = Node(3)
root.right = Node(5)
root.left.left  =  Node(8)
