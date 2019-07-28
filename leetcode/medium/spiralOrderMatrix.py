class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        b = n
        ic = 0
        jc = n-1
        ir = 0
        jr = n-1
        k = 0
        while b>0:
            for i in range(ic,jc+1):
                k+=1
                ans[ir][i] = k
            for i in range(ir+1,jr):
                k+=1
                ans[i][jc] = k
            for i in range(jc,ic,-1):
                k+=1
                ans[jr][i] = k
            for i in range(jr,ir,-1):
                k+=1
                ans[i][ic] = k
            b -= 2
            ic +=1
            jc -=1
            ir +=1
            jr -=1
        return ans
