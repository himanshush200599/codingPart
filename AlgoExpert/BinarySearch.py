# Recursive solution for binary search algorithms
# Time complexity -  O(logN)
# Space complexity - O(logN) for call stack during recursive call

def BinarySearch(ar,target):
    return BinarySearchHelper(ar,target,0,len(ar)-1)

def BinarySearchHelper(ar,target,l,r):
    if l>r:
        return -1
    mid = (l+r)//2
    curr = ar[mid]
    if curr == target:
        return mid
    elif curr>target:
        return BinarySearchHelper(arr,target,mid+1,r)
    else:
        return BinarySearchHelper(ar,targer,l,mid-1)
