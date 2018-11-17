def lcs(s1, s2):
    """
        s1 and s2 are two strings.
        Finds the longest common subsequence of s1 and s2
    """
    l1 = len(s1)
    l2 = len(s2)

    # when both strings are empty
    if l1 == 0 and l2 == 0:
        return 0

    L = [[0 for i in range(l2+1)] for j in range(l1+1)]

    # Trivial cases
    for i in range(l2+1):
        L[0][i] = 0

    for j in range(l1+1):
        L[j][0] = 0

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    print_seq(L, s1, s2)
    print("Length of LCS: ", L[l1][l2])
    return L[l1][l2]


def print_seq(L, s1, s2):
    """ Prints the longest common subsequence """
    lcs = ""

    i = len(L) - 1
    j = len(L[0]) - 1

    while True:
        if i == 0 or j == 0:
            break
        elif s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif L[i][j-1] > L[i-1][j]:
            j -= 1
        else:
            i -= 1
    print(lcs)
def main():
    lcs('abcdaf','acbcf')

main()







# my solution based on H.CORMEN
# | is for upper arrow # / is for  diagonal  arrow # -- is for side arrow
def LCS_LENGTH(input1,input2):
    len1 = len(input1)
    len2 = len(input2)
    c = [[0 for i in range(len2+1)] for j in range(len1+1)]
    b = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(1,len2+1):
        c[0][i] = 0
    for j in range(0,len1+1):
        c[j][0] = 0
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if input1[i-1] == input2[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
                b[i][j] = 'D'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'U'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'L'
    print("sequence is -")
    print_seq(b,input1,len1,len2)

def print_seq(b,input1,i,j):
    if i==0  and  j==0:
        return
    if b[i][j] == "D":
        print_seq(b,input1,i-1,j-1)
        print(input1[i])
    elif b[i][j] == 'U':
        print_seq(b,input1,i-1,j)
    else:
        print_seq(b,input1,i,j-1)
LCS_LENGTH('abcbdab','bdcaba')
