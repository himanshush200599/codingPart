# Here i am going to implement recursive solution for the same

def validateBST(root):
    return validateBSTHelper(root,float("-inf"),float("inf"))

def validateBSTHelper(root,mini,maxi):
    if root is None:
        return True
    if root.value < mini or root.value >=maxi:
        return False
    IsLeftValid = validateBSTHelper(root.left,mini,root.value)
    return IsLeftValid and validateBSTHelper(root.right,root.value,maxi)