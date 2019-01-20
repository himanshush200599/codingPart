def valid(maze,visited,rowNew,colNew):
    if rowNew>=0 and colNew>=0 and colNew<4 and rowNew<4 and (not visited[rowNew][colNew]) and (maze[rowNew][colNew]==1):
        return True
    else:
        return False
def ratAndMaze(maze,visited,row,col,desRow,desCol,move):
    if row==desRow and col==desCol:
        for i in range(4):
            for j in range(4):
                print(visited[i][j],end= " ")
            print()
        print("##########################################")
    else:
        for i in range(len(pathRow)):
            rowNew = row+pathRow[i]
            colNew = col+pathCol[i]
            if valid(maze,visited,rowNew,colNew):
                move+=1
                visited[rowNew][colNew] = move
                ratAndMaze(maze,visited,rowNew,colNew,desRow,desCol,move)
                move-=1
                visited[rowNew][colNew] = 0

pathRow = [0,0,1,-1]
pathCol = [1,-1,0,0]
maze = [[1,1,0,1],[0,1,1,1],[0,1,0,1],[0,1,1,1]]
visited = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

ratAndMaze(maze,visited,0,0,3,3,1)
