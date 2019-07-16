class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromicSS(str):
            currentLongest = [0,1] #starting and ending index of current lngest 1(Exclusive)
            for i in range(1,len(str)):
                odd =  getLongestPalindrom(str,i-1,i+1)
                even =  getLongestPalindrom(str,i-1,i)
                longest = max(odd,even,key=lambda x: x[1]-x[0])
                currentLongest = max(longest,currentLongest,key=lambda x: x[1]-x[0])
            return str[currentLongest[0]:currentLongest[1]]

        def getLongestPalindrom(str,i,j):
            while i>=0 and j<len(str):
                if str[i]!=str[j]:
                    break
                i-=1
                j+=1
            return [i+1,j]
        return longestPalindromicSS(s)
        
