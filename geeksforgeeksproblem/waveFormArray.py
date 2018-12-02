"""
Input:  arr[] = {20, 10, 8, 6, 4, 2}
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4} OR
                 any other array that is in wave form

"""
def waveForm(a,n):
    a.sort()
    for i in range(0,n,2):
        a[i],a[i+1] = a[i+1],a[i]
    print(a[0:])
waveForm([20,10,8,6,4,2],6)

# another approach is to  check all even index elemensts and then
# compare them with prevois and next to them
# swap in both cases if it is smaller than it .
