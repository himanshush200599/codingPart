class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanToInteger = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        i = 0
        while i < len(s)-1:
            if romanToInteger[s[i]] >= romanToInteger[s[i+1]]:
                total += romanToInteger[s[i]]
                i += 1
            else:
                total += romanToInteger[s[i+1]] - romanToInteger[s[i]]
                i += 2
        if i == len(s)-1:
            total += romanToInteger[s[i]]
        return total
