"""
Here we have to find leaders from array i,e no other element from in the right side of array will not be greater
than it.
"""

for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    z = []
    for i in range(n):
        if (l[i] == max(l[i:])):
            if l[i] not in z:
                z.append(l[i])
    for i in z:
        print(i,end=" ")
