# this is naive approach where
# we are checking by sorting both the strings

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)
#efficient way by using set
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0 and len(t) ==0:
          return True
        elif len(s)==len(t):
          p=set(s)
          q=set(t)


          if p==q:
            for i in p:
                if s.count(i)==t.count(i):
                     return True
                else:
                     return False
          else:
             return False
        else:
            return False
