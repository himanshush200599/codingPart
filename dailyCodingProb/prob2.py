"""
Given an array of integers, return a new array such that each element at index i of the
 new array is the
 product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
 would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

"""
asked by Uber
"""
class Prob2(object):
    """docstring for Prob2."""
    def __init__(self, l):
        super(Prob2, self).__init__()
        self.l = l
    def newArray(self):
        """
        time complexity=O(n*n)
        design by - himanshu sharma
        without divisor and with divisor
        """
        m = []
        s = 1
        for i in range(len(self.l)):
            for j in range(len(self.l)):
                if i!=j:
                  s = s*self.l[j]

            m.append(s)
            s = 1
        return m

    def newArray1(self):
        """
        source - Pulkit bhaiya
        Time complexity - O(n)
        
        """
        s =1
        m = []
        for i in range(len(self.l)):
            s = s*self.l[i]
        for i in range(len(self.l)):
            m.append(s//self.l[i])
        return m



a = Prob2([3,2,1])
print(a.newArray1())
