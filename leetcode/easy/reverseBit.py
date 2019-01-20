class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:][::-1]
        if len(n)<32:
            n = n+'0'*(32-len(n))
        return  int(n,2)
