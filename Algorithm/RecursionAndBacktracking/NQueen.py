
def valid(board,newRow,newCol,size):
    valid  = True
    for i in range(size):
        if board[i][newCol]:
            valid = False
    i,j = newRow,newCol
    while j>=0 and i>=0:
        if(board[i][j]):
            valid = False
        i-=1
        j-=1
    i,j = newRow,newCol
    while j>=size and i>=0:
        if(board[i][j]):
            valid = False
        i-=1
        j+=1

    return valid
def NQueen(board,size,row):
    if row==size-1:    #row=0 start
        for i in range(size):
            for j in range(size):
                print(board[i][j],end=" ")
            print()
        print("####################################")
        return True
    else:
        for col in range(size):
            newRow  = row+1
            if valid(board,newRow,col,size):
                board[newRow][col] = True
                if(NQueen(board,size,newRow)):
                    return True
                board[newRow][col] = False
        return  False
size = 16
board = [[False for i in range(size)] for j in range(size)]
NQueen(board,size,-1)
