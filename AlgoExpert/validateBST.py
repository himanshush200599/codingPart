# Here i am going to implement recursive solution for the same
# Just compare value of every node with minimum and maximum around them
def validateBST(root):
    return validateBSTHelper(root,float("-inf"),float("inf"))

def validateBSTHelper(root,mini,maxi):
    if root is None:
        return True
    if root.value < mini or root.value >=maxi:
        return False
    IsLeftValid = validateBSTHelper(root.left,mini,root.value)
    return IsLeftValid and validateBSTHelper(root.right,root.value+1,maxi)
