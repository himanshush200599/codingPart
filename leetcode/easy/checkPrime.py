# not so efficient

import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def checkprime(x):
            if x==1:
                return False
            if x==2 or x==3:
                return True
            if x%2==0:
                return False
            if x%3==0:
                return False
            if x<9:
                return True

            k=5
            f=math.floor(math.sqrt(x))

            while(k<=f):
                if(x%k==0):
                    return False
                if(x%(k+2)==0):
                    return False
                k+=6
            return True
        c = 0
        for  i in range(1,n):
            if checkprime(i):
                c+=1
        return c
