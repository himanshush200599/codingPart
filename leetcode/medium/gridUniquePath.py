class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        c=[]

        for i in range(A):
            c.append([1]*B)

        for j in range(1,B):
            for i in range(1,A):
                c[i][j] = c[i][j-1] + c[i-1][j]

        return c[A-1][B-1]
