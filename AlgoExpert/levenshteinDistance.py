# also called Edit-Distance problem
# dp solution with time and space complexity O(NM)
def EditDistance(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0 for i in range(n2+1)] for _ in range(n1+1)]
    for i in range(n2+1):
        dp[0][i] = i
    for i in range(n1+1):
        dp[i][0] = i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n1][n2]

print(EditDistance("abc","yabd"))
