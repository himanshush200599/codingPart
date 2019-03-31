class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        symb = 'abcdef'
        num &= 0xFFFFFFFF #masking so that negetive number can also be converted like -1==64
        res = []
        while num:
            cur = num % 16
            res.append(str(cur) if cur < 10 else symb[cur-10])
            num //= 16
        return ''.join(res[::-1]) if res else '0'
