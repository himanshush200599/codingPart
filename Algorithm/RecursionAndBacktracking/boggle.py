# #this problem can be solved using backtracking(recusrion)
# in this we have a grid(m*n) and a dictionary
# then we have to print all valid word form from grid by traversing
# and if this word present in dictionary then it is valid
# print all valid words


def valid(rowNew,colNew,visited):
    if(rowNew>=0 and colNew>=0 and colNew<3 and rowNew<3 and (not visited[rowNew][colNew])):
        return True
    else:
        return False
def  findWord(board,visited,row,col,word,engD):
    #print(word)
    if word  in engD:
        print(word)

    for m in range(len(pathRow)):
        rowNew = row+pathRow[m]
        colNew = col+pathCol[m]
        if valid(rowNew,colNew,visited):
            visited[rowNew][colNew] = True
            findWord(board,visited,rowNew,colNew,word+board[rowNew][colNew],engD)
            visited[rowNew][colNew] = False
pathRow = [0,0,1,1,-1,1,-1,-1]
pathCol = [1,-1,-1,1,1,0,0,-1]
board =[['g','i','z'],['u','e','k'],['q','s','e']]
visited = [[False,False,False ],[False,False,False ],[False,False,False ]]
engD = ['geeks','quiz','for','go','gek','euge']
word = ''
for i in range(3):
    for j in range(3):
        visited[i][j]  = True
        findWord(board,visited,0,0,word+board[i][j],engD)
        visited[i][j] = False
