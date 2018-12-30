# generate matrix in diagonal fashion
# half the matrix diagonnally and then fill
# december lunchtime challenge  problem 1

for _ in range(int(input())):
    n = int(input())
    l = [[0 for j in range(n)] for i in range(n)]
    p = 1
    for k in range(n):
        i = k
        j = 0
        while i>=0:
            l[j][i] =p
            p+=1
            i-=1
            j+=1
    for k in range(1,n):
        i = n-1
        j = k
        while j<=n-1:
            l[j][i] =p
            p+=1
            i-=1
            j+=1
    for i in range(n):
        for j in range(n):
            print(l[i][j],end=' ')
        print()
