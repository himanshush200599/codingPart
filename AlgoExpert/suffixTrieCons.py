class SuffixTrie:
    def __init__(self,string):
        self.string  = string
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Time and space is O(N^2)
    def populateSuffixTrieFrom(self,string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i,string)

    def insertSubstringStartingAt(self,i,string):
        node =  self.root
        for j in range(i,len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True


    # Time complexity = O(M)||space = O(1) where m is length of string to be search
    def contains(self,string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
