class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        i=0
        q=[root,]
        k=1
        ans=[]
        avg=0.0
        while(q):
            while(i<k):
                root=q.pop(0)
                i+=1
                if root:
                    avg+=root.val
                    
                    if root.left and root.right:
                        q.append(root.left)
                        q.append(root.right)
                    elif root.left:
                        q.append(root.left)
                    elif root.right:
                        q.append(root.right)
                    else:
                        pass
            print(avg,k)
            avg=avg/k           
            ans.append(avg)
            avg=0.0
            k=len(q)
            i=0
        return ans
