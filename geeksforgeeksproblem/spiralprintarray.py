"""
print array in spiral order.
"""

for _ in range(int(input())):
    n = 4
    #l1 = [list(map(int,input().split())) for row in range(n)]
    l1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]
    l = 0
    r = n-1
    t = 0
    b= n-1
    dir = 0
    while l<=r and t<=b:
        if dir == 0:
            for i in range(l,r+1):
                print(l1[t][i],end = ' ')
            t+=1
            dir = 1
        elif dir == 1:
            for i in range(t,b+1):
               print(l1[i][r],end = ' ')
            r-=1
            dir = 2
        elif dir == 2:
            for i in range(r,l-1,-1):
               print(l1[b][i],end=' ')
            b-=1
            dir = 3
        elif dir == 3:
            for i in range(b,t-1,-1):
               print(l1[i][l],end=' ')
            l+=1
            dir = 0
    print()
