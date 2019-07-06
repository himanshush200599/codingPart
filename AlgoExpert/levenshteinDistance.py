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


# optimised space complexity from O(NM) to O(min(N,M))

def EditDistance(str1,str2):
    small = str1  if len(str1)<len(str2) else str2
    big = str1  if len(str1)>len(str2) else str2
    dpEven = [x for x in range(len(small)+1)]
    dpOdd = [None for _ in range(len(small)+1)]
    for i in range(1,len(big)+1):
        if i%2==0:
            dpCurrent = dpOdd
            dpPrevious = dpEven
        else:
            dpCurrent = dpEven
            dpPrevious = dpOdd
        dpCurrent[0] = i
        for j in range(len(small)+1):
            if big[i-1]==small[i-1]:
                dpCurrent[j] = dpPrevious[j-1]
            else:
                dpCurrent[j] = 1+min(dpPrevious[j-1],dpPrevious[j],dpCurrent[j-1])
    return dpEven[-1] if len(big)%2==0 else dpOdd[-1]
