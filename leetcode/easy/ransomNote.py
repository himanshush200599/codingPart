# my solution using hash map 
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for i in ransomNote:
            if d[i]>=ransomNote.count(i):
                pass
            else:
                return False
        return True
