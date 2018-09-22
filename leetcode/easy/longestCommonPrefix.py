class Solution:
        def longestCommonPrefix(self,strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            """
                1.find length of all string
                2. Loop from smallest lenght string and pick charcter by character and compare them
                3.if all the characters till now are same then add it to empty string
                4. return if matching doesnot occur between character array.
            """
            if len(strs)==0:
                return ""
            if len(strs)==1:
                return strs[0]
            cp = ''
            l = [len(st) for st in strs]
            for i in range(min(l)):
                tmp = [s[i] for s in strs]
                if min(tmp)==max(tmp): #check if all of them are the same
                    cp = cp + tmp[0]
                else:
                    return cp
            return cp


        def longestCommonPrefix2(self, strs):
            """ Vertical scanning algorithm. """
            if not strs:
                return None

            # for each character in strs[0] at position i, compare it with
            # character at i-th position for all the strings.
            for i in range(len(strs[0])):
                char = strs[0][i]
                for j in range(1, len(strs)):
                    if i >= len(strs[j]) or strs[j][i] != char:
                        return strs[0][:i]
a = Solution()
print(a.longestCommonPrefix2(['leetcode','leet','lee']))
