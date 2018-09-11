def merge(a,l,m,r):
    n1 = m-l+1
    n2 = r-m
    L = [0]*n1
    R = [0]*n2
    for i in range(0,n1):
        L[i] = a[l+i]
    for j in range(0,n2):
        R[j] = a[m+1+j]
    i = 0 #index for left aaray
    j = 0 #index for right array
    k = l #index for sorted array

    while i<n1 and j<n2:
        if L[i]<R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            j+=1
        k+=1
        #incase of odd lenght array if any element left.
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1


    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
def mergeSort(a,l,r):
    if l<r:
        m = int((l+(r-1))/2)
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

def main():
    arr = [12, 11, 13, 5, 6, 7]
    n = int(len(arr) )
    print ("Given array is")
    print(arr)

    mergeSort(arr,0,n-1)
    print ("\n\nSorted array is")
    print(arr)
main()
