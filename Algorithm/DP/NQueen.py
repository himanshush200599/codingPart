x = []
def NQueen(k,n):

    for i in range(1,n+1):
        if(Place(k,i)):
            x[k] = i
            if  k == n:
                print(x[1:n])
            else :
                NQueen(k+1,n)
def Place(k,i):
    for j in range(1,k):
        if(x[j] ==  i or (abs(x[j]-i)) - abs(j-k)):
            return False
    return True
NQueen(1,8)


# Not working
# this need modification
# added in to do list
