# Time complexity - O(N^2)
# Space complexity - O(1) Inplace sorting algorithms

def InsertionSort(ar):
    for i in range(1,len(ar)):
        j = i
        while j>0 and ar[j]<ar[j-1]:
            swap(j,j-1,ar)
            j-=1
    return ar

def swap(i,j,ar):
    ar[i],ar[j] = ar[j],ar[i]
