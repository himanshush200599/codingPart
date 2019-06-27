# Time complexity - O(NlognN + MlogM)
# for sorting both the arrays
# Space complexity - O(1)

def smallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    i1 = 0
    i2 = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while i1<len(array1) and i2<len(array2):
        n1 = array1[i1]
        n2 = array2[i2]
        if n1>n2:
            current = n1-n2
            i1+=1
        elif n2>n1:
            current = n2-n1
            i2+=1
        else:
            return [n1,n2]
        if smallest>current:
            smallest  = current
            smallestPair= [n1,n2]
    return smallestPair

print(smallestDifference([1,2,4,2,4,22,21,2],[5,3,4,8,24,2,4,9,3]))
