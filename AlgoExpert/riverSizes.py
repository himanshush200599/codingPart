def riverSizes(matrix):
    res = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,res)
    return res


def traverseNode(i,j,matrix,visited,res):
    currRiverSize = 0
    nodeToTraverse = [[i,j]]
    while len(nodeToTraverse):
        currentNode = nodeToTraverse.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j]==0:
            continue
        currRiverSize+=1
        unvisitedNeighbours = getUnvisitedNeighbours(i,j,matrix,visited)
        for neighbour in unvisitedNeighbours:
            nodeToTraverse.append(neighbour)
    if currRiverSize>0:
        res.append(currRiverSize)

def getUnvisitedNeighbours(i,j,matrix,visited):
    unvisitedNeighbours = []
    if i>0 and not visited[i-1][j]:
        unvisitedNeighbours.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:
        unvisitedNeighbours.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unvisitedNeighbours.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedNeighbours.append([i,j+1])
    return unvisitedNeighbours
