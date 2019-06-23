def BubbleSort(arr):
    isSorted = False #pause when array is sorted instead checking for all elements
    counter = 0 #Decrease number of checks for sorted array by ignoring counter 
    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1-counter):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                isSorted  = False
        counter+=1
    return arr
print(BubbleSort([2,4,1,9,6,5,0,5]))
