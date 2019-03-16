class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordList = str.split()
        n1 = len(pattern)
        n2 = len(wordList)
        if (n1 != n2):
            return False
        else:
            mydict = {}
            result = True
            for i in range(len(pattern)):
                if (pattern[i] not in mydict):
                    if wordList[i] not in mydict.values():
                        mydict[pattern[i]] = wordList[i]
                    else:
                        result = False
                        break
                else:
                    if (mydict[pattern[i]] != wordList[i]):
                        result = False
                        break
            return result
