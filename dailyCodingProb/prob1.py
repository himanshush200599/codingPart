"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

class Prob1(object):
    """docstring for Prob1."""
    def __init__(self, l,k):

        self.l =  l
        self.k = k

    def check4k(self):
        """
            this takes O(n*n) for time complexity
            simple method is used by comparing each elemnt with everry other element
             and check for sum if it is equal to k or not
             Made by self
        """
        for i in range(len(self.l)):
            for j in range(i+1,len(self.l)):
                if((self.l[i] + self.l[j])==self.k):
                    return True
        return False

    def printPairs(self):

    # Create an empty hash set
        """
        method used - hashing
        time complexity - O(n)
        Help from geeksforgeeks
        design by self

        """
        s = set()

        for i in range(len(self.l)):
            temp = self.k-self.l[i]
            if (temp>=0 and temp in s):
                print ("Pair which are equal to " ,self.k, "are " ,self.l[i], "and", temp)
            s.add(self.l[i])

    """
        Another method is -
            1. Sort the array
            2. then assign indeces to 2 variable-
                a. l = 0
                b.  r = len(l)-1
            3.then compare with l and r indices elements and if sum equal (arr[l]+arr[r]) then
            return true .
            if small then l++
            if large r--
    """
a = Prob1([10,15,3,7,8],27)
print(a.check4k())
a.printPairs()
