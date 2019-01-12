class Solution:
    def isPalindrome(self, s):
        res = ""
        for c in s:
            if c.isalnum():
                res = res + c
        return res.lower() == res[::-1].lower()
