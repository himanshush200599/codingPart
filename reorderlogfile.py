class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        X,Y=[],[]
        for i in logs:
            if i.split()[1].isdigit():
                X.append(i)
            else:
                Y.append(i)
        Y.sort(key = lambda x: x.split()[1])
        Y.sort(key = lambda x: x.split()[1:])
        return Y+X
