"""
Given an unsorted array of size N. Find the first element in array such that all of its left elements
are smaller and all right elements to it are greater than it.

Note: Left and right side elements can be equal to required element. And extreme elements cannot
be required element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array
 and the second line contains N space separated array elements.

Output:
For each test case, in a new line print the required element. If no such element present in array then print -1
.

Constraints:
1<=T<=100
3<=N<=106
1<=A[i]<=106

Example:
Input:
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9

Output:
5
-1
7
"""
# solution source - geeksforgeeks
for _ in range(int(input())):
    n  = int(input())
    arr = list(map(int,input().split()))
    l=[0]*n
    r=[0]*n
    l[0]=arr[0]
    r[n-1]=arr[n-1]
    for i in range(1,n):
        l[i]=max(l[i-1],arr[i])
    for i in range(n-2,-1,-1):
        r[i]=min(r[i+1],arr[i])
    flag=0
    # print l
    # print r
    for i in range(1,n-1):
        if arr[i]>=l[i-1] and arr[i]<=r[i+1]:
            print (arr[i])
            flag=1
            break
    if flag==0:
        print (-1)
