"""
Heap- An array visualised as a nearly complete binary tree
root of the tree i,e first element (i=1)
parent(i) = int(i/2)
left(i)- 2*i    #when index is start from 1.
right(i) - 2*i + 1

MAX_HEAP-
key of the node is gretaer than or equal to the key of its children.

"""
def Heapify(a,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and a[i]<a[l]:
        largest = l

    if r<n and a[largest]<a[r]:
        largest = r
    if largest !=i :
        a[largest],a[i] = a[i],a[largest]
        Heapify(a,n,largest)


def HeapSort(a):
    n = len(a)
    for i in range(n,-1,-1):
        Heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0] = a[0],a[i]
        Heapify(a,i,0)
    print(a)
HeapSort([2,8,1,3,7,9])
