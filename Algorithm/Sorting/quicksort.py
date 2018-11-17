def quicksort(a,low,high):
    if low<high:
        r  = partition(a,low,high)
        quicksort(a,low,r-1)
        quicksort(a,r+1,high)
    return a
def partition(a,low,high):
    pivot = a[high]
    i = low-1
    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[j],a[i] = a[i],a[j]
    a[i+1],a[high] = a[high],a[i+1]
    return i+1
print(quicksort([5,7,1,3,9,3],0,5))
