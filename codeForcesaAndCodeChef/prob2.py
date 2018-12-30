def printMatrixDiagonal(mat, n):
    i = 0
    j = 0
    k = 0
    z= 1
    isUp = True
    while k<n*n:

        if isUp:
            while i >= 0 and j<n :
                mat[i][j] = z
                z+=1
                k +=1
                j +=1
                i -=1


            if i < 0 and j <= n - 1:
                i = 0
            if j == n:
                i = i+2
                j -= 1

        if isUp:
            while j >= 0 and i<n :
                mat[i][j] = z
                z+=1
                k += 1
                i += 1
                j -= 1


            if j < 0 and i <= n - 1:
                j = 0
            if i == n:
                j = j + 2
                i -= 1
        isUp = isUp
