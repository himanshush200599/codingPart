# Time complexity - O(N^2)
# Space complexity - O(1) Inplace sorting algorithms

def SelectionSort(arr):
    curr = 0
    while curr<len(arr)-1:
        mini = curr
        for i in range(curr+1,len(arr)):
            if arr[i]<arr[curr]:
                arr[i],arr[curr] = arr[curr],arr[i]
        curr+=1
    return arr

print(SelectionSort([2,1,3,8,9,6,7,4,6,5]))
