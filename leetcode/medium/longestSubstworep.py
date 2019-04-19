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
        def checkUniqueChar(string,index):
            # this function take every substring and return maximum
            # length of uniquw characters
            st = set()
            for i in range(index,len(string)):
                if string[i] not in st:
                    st.add(string[i])
                else:
                    return i-index
            return len(string)-index
        maxL  = 0
        for i in range(len(s)):
            # calling checkUniqueChar function for every substring
            maxL = max(maxL,checkUniqueChar(s,i))
        return maxL


# Efficient approach
# using sliding window approach
# Time complexity - O(N)
# we are maintaining a hash map and modifiying it whenver we found character which
# is already in hash map.We are sliding window accordingly
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash = {}
        start = 0
        maxL = 0
        for end in range(len(s)):
            if s[end] in hash:
                start = max(start,hash[s[end]]+1)
            hash[s[end]] = end
            maxL = max(maxL,end-start+1)
        return maxL
