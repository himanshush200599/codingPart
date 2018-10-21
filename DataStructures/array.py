class Array:

    def __init__(self, arr):
        super(Array, self).__init__()
        self.arr = arr
    def CreateArray(self):
        l = int(input("Enter no of element you want to insert in array "))
        for i in range(l):
            k = int(input('Enter '+ str(i)+'th element for array '))
            self.arr.append(k)
    def PrintArray(self):
        for i in range(len(self.arr)):
            print(self.arr[i])
    def InsertElement(self):
        k = int(input('Enter element to insert'))
        self.arr.append(k)
    def DeleteElement(self):
        s = self.arr[-1]
        self.arr.pop()
        print("deleted element is "+str(s))
    def DeleteElementIndex(self):
        index=int(input('Enter index of element you want to delete'))
        for i in range(index,len(self.arr)-1):
            self.arr[i] = self.arr[i+1]

        self.arr.pop()
    def InsertElementIndex(self):
        index=int(input("Enter index at which you want to insert element"))
        element= int(input('Enter element to insert'))
        e  = self.arr[-1]
        for i in range(index,len(self.arr)-1):
            self.arr[i+1]=self.arr[i]
        self.arr[index] = element
        self.arr.append1(e)
a  = Array([])
a.CreateArray()
a.PrintArray()
a.InsertElement()
a.PrintArray()
a.DeleteElement()
a.PrintArray()
a.DeleteElementIndex()
a.PrintArray()
a.InsertElementIndex()
a.PrintArray()
