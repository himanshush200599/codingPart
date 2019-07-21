# Credit - leetcode discussion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows>=len(s):
            return s
        res = ['']*numRows
        row = 0
        for char in s:
            res[row] +=char
            if row == 0:
                step = 1   #going down
            elif row==numRows-1:
                step=-1   #going up
            row+=step
        return ''.join(res)
