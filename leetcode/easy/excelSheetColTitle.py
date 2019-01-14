class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {
            1:'A',
            2:'B',
            3:'C',
            4:'D',
            5:'E',
            6:'F',
            7:'G',
            8:'H',
            9:'I',
            10:'J',
            11:'K',
            12:'L',
            13:'M',
            14:'N',
            15:'O',
            16:'P',
            17:'Q',
            18:'R',
            19:'S',
            20:'T',
            21:'U',
            22:'V',
            23:'W',
            24:'X',
            25:'Y',
            26:'Z'


        }
        a = n
        s = ''
        while a>0:
            if a%26:
                s = s+d[a%26]
                a = int(a/26)
            else:
                s = s+'Z'
                a = int(a/26-1)

        return s[::-1]
a = Solution()
print(a.convertToTitle(7))
