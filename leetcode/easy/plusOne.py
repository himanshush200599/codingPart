class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = []
        digits = map(str,digits)
        dig = ''.join(digits)
        dig = int(dig)
        dig+=1
        dig = str(dig)
        for c in dig:
            l.append(c)
        for i in range(len(l)):
            l[i] = int(l[i])
        return l
