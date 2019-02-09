# i  tried it with 1 map but failed on edge cases
# this is kunal bhaiya  solution
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapped = set()
        mappings = {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            # if current character is already mapped, then check its value
            if s[i] in mappings:
                if mappings[s[i]] != t[i]:
                    return False
            # if current char is not mapped, check whether some other char
            # is mapped to the same value
            else:
                if t[i] in mapped:
                    return False
                mappings[s[i]] = t[i]
                mapped.add(t[i])
        return True
