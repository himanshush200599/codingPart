'''
Insertion sort -
Time complexity -
1. Best Case - O(n)
2. Worst Case - O(n*n)

take a key from unsoretd array and compare it with all the element in left sub-subarray
and insert it in its right position.
'''
class InsertionSort(object):
    """docstring for InsertionSort."""
    def __init__(self, a,n):
        super(InsertionSort, self).__init__()
        self.a = a
        self.n = n
    def sort(self):
        for i in range(1,self.n):
            key = self.a[i]
            j = i-1
            while j>=0 and self.a[j]>key:
                self.a[j+1]=self.a[j]
                j = j-1
            self.a[j+1] = key
        return self.a
    def printSorted(self):
          res = self.sort()
          print(res)
a = InsertionSort([int(x) for x in input().split()],6) #n is variable we can store it in variable and then
                                                        #pass in class
a.printSorted()
