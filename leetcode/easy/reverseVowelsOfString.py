class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = 0
        z = len(s)-1
        d = set(['a','e','i','o','u','A','E',"I","O","U"])
        s = list(s)
        while a<=z:
            if s[a]  in d and s[z]  in d:
                s[a],s[z] = s[z],s[a]
                a+=1
                z-=1
            elif s[a] in d:
                z-=1
            else:
                a+=1
        return "".join(s)
