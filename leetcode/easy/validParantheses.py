class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
            Here i am using Stack to store symbols and then pop by comparing
        """
        stack = []
        for i in s:
            if i == '[' or i == '{' or i == '(':
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif len(s) ==1:
                    return False
                elif ((i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or (i == "}" and stack[-1] == "{")) :
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
