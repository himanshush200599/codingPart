class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        o,e=1,0
        n=len(A)
        l=[0]*n
        for i in A:
            if i%2==0:
                l[e]=i
                e+=2
            else:
                l[o]=i
                o+=2
        return l
                
            
 #--------------------------------------------------------#
 
A=[4,2,5,7]
j = 1
for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
print(A)
