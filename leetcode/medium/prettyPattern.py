

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2*A-1
        temp = 0
        l = [[0 for x in range(size)] for y in range(size)]
        while A>0:
            for i in range(temp,size):
                for j in range(temp,size):
                    l[i][j]=A
            A-=1
            size-=1
            temp+=1


        return l
# print(Solution().prettyPrint(3))
