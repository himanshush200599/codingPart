import collections
class Stack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)
    def printQ(self):
        for i in self._queue:
            print(i)
a = Stack()
print(a.push(3))
print(a.push(4))
print(a.push(5))
print(a.push(6))
print(a.pop())
print(a.top())
print(a.pop())
print(a.push(0))
print(a.printQ())
