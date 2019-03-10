def match(s,p):
        res = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        res[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                res[0][i] = res[0][i - 1]
            else:
                res[0][i] = False
        for i in range(1, len(s) + 1):
            res[i][0] = False
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    res[i][j] = res[i - 1][j - 1]
                elif p[j - 1] == '*':
                    res[i][j] = res[i - 1][j] or res[i][j - 1]
                else:
                    res[i][j] = False
        return res[len(s)][len(p)]
print(match("fgfgfg","*gfg"))
