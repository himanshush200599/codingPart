class Node:
    def __init__(self,name):
        self.name = name
        self.children = []
    def addChild(self,name):
        self.children.append(Node(name))
    def breadthFirstSearch(self,array):
        queue = [self]
        while len(queue)>0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
