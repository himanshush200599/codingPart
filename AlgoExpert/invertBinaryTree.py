# iterative solution for tree invert problem
def invertBinaryTree(root):
    queue = [root]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        # swapping here
        current.left,current.right = current.right,current.left
        queue.append(current.left)
        queue.append(current.right)
    return root

# Recursive solution for the same
def invertTree(root):
        if root:
            root.left, root.right = invertTree(root.right),invertTree(root.left)
        return root
