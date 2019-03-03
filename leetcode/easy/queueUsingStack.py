class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.l.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        s = self.l[0]
        self.l = self.l[1:]
        return s


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.l)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
