# here we have  to find no of ways to reach bottom of a 20X20 grid
# Here i am using dynamic Problem to solve this
def countWays(n):
    grid  = [[0  for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        grid[0][i] = 1
    for i in range(n+1):
        grid[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            grid[i][j] = grid[i-1][j]+grid[i][j-1]
    return grid[n][n]
print(countWays(2))
# favrote problem till now i have solved 
