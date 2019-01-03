class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res =[]
        if root != None:
            dq = deque()
            dq.append(root)
            while len(dq) > 0:
                temp = []
                size = len(dq)
                for i in range(size):
                    cur = dq.pop()
                    temp.append(cur.val)
                    if cur.left != None:
                        dq.appendleft(cur.left)
                    if cur.right != None:
                        dq.appendleft(cur.right)
                res.append(temp)
            res.reverse()



        return res

        
