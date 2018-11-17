# not a couting sort but it  sorts array on the concept of couting sort
# i design it myself
# accrdng to count of element i print that element
def countingSortKids(arr):
    k = 0
    n = len(arr)
    k = max(arr)+1
    auxArray = [0]*k
    for i in range(n):
        if auxArray[arr[i]]==0:
            auxArray[arr[i]] = 1
        else:
            auxArray[arr[i]] = auxArray[arr[i]] + 1
    for i in range(len(auxArray)):
            while auxArray[i]!=0:
                print(i)
                auxArray[i] = auxArray[i]-1
countingSortKids([3,1,3,1,5,8,5])
