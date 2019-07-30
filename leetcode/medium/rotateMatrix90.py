class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        B = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                B[j][n-i-1] = A[i][j]

        return B
