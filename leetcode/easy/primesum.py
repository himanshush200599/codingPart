class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        prime = [True for i in range(0, A + 1)]

        p = 2
        while p * p < A:
            if prime[p]:
                for i in range(p * p, A + 1, p):
                    if prime[i]:
                        prime[i] = False
            p += 1

        if len(prime) > 1:

            prime[0] = False
            prime[1] = False

        for i in range(2, A+1):

            if prime[i] and prime[A-i]:
                return [i, A-i]
