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
