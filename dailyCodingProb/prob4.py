"""
Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

"""

class Prob4(object):
    """docstring for Prob4.

    Time complexity- O(nlogn)
    """
    def minimumMissing(self):
        l = list(map(int,input().split()))
        l.sort()
        if 1 not in l:
                print("1")
        else:
            for i in range(len(l)-1):
                if (l[i+1]-l[i])>1:
                    print(l[i]+1)
                    break
                elif(i == len(l)-2):
                    print(l[len(l)-1]+1)
a = Prob4()
a.minimumMissing()
