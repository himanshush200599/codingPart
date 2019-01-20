# problem of horse(LOL) in chess
# in how many ways he roam in whole chase
# using recursion(Backtraking)

# GOT
# KNIGHT-TOUR
def valid(rowNew,colNew,visited):
    if rowNew>=0 and colNew>=0 and rowNew<8 and colNew<8 and visited[rowNew][colNew]==0:
        return True
    return False
def knightTour(visited,row,col,move):
    if move ==64:  #because we are taking 8*8 chess
        for i in range(8):
            for j in range(8):
                print(visited[i][j],end=" ")
            print()

        print('######################################')
        return True
    else:
        for i in range(len(pathRow)):
            rowNew = row + pathRow[i]
            colNew = col + pathCol[i]
            if valid(rowNew,colNew,visited):
                move+=1
                visited[rowNew][colNew] = move
                # knightTour(visited,rowNew,colNew,move) these lines are working finw but taking s much time
                # move -=1
                # visited[rowNew][colNew] = 0
                if (knightTour(visited,rowNew,colNew,move)):
                    return True
                move-=1
                visited[rowNew][colNew] = 0
    return False
pathRow = [2,1,-1,-2,-2,-1,1,2]
pathCol = [1,2,2,1,-1,-2,-2,-1]
visited = [[0 for i in range(8)] for j in range(8)]
visited[0][0] = 1
knightTour(visited,0,0,1)
