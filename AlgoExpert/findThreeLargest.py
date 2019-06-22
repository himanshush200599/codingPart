def findThreeLargest(arr):
    result = [None,None,None]
    for num in arr:
        updateResult(result,num)
    return result
def updateResult(result,num):
    if result[2] is None or result[2]<num:
        shiftAndUpdate(result,num,2)
    elif result[1] is None or result[1]<num:
        shiftAndUpdate(result,num,1)
    elif result[0] is None or result[0]<num:
        shiftAndUpdate(result,num,0)
    print(result)
def shiftAndUpdate(arr,num,ind):
    for i in range(ind+1):
        if ind==i:
            arr[i] = num
        else:
            arr[i] = arr[i+1]
print(findThreeLargest([2,3,6,1,89,1,90,112,3,70]))
