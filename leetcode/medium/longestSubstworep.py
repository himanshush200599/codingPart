# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#First we have brute force approach
# It give TLE for  large Input
# This solution has time complexity of O(N*N)
# O(N) is for checkUniqueChar and O(N) for calling checkUniqueChar each time
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def checkUniqueChar(string,index):
            st = set()
            for i in range(index,len(string)):
                if string[i] not in st:
                    st.add(string[i])
                else:
                    return i-index
            return len(string)-index
        maxL  = 0
        for i in range(len(s)):
            maxL = max(maxL,checkUniqueChar(s,i))
        return maxL
