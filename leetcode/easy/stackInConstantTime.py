class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [None]


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # update min pointer
        if self.min_stack[-1] is None or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        el = self.stack.pop()
        # update min pointer
        if el == self.min_stack[-1]:
            _ = self.min_stack.pop()

        return el


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
