"""

    Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.


Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
 Each test case consists of two lines. The first line of each test case is N and S, where N is the size of
 array and S is the sum. The second line of each test case contains N space separated integers denoting the
 array elements.

Output:

Corresponding to each test case, in a new line, print the starting and ending positions of first such
occuring subarray if sum equals to subarray, else print -1.

Note: Position of 1st element of the array should be considered as 1.

Expected Time Complexity: O(n)

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ an array element ≤ 200

Example:

Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10

Output:
2 4
1 5

Explanation :
In first test case, sum of elements from 2nd position to 4th position is 12
In second test case, sum of elements from 1st position to 5th position is 15
"""


for i  in range(int(input())):
    n,s = input().split()
    n,s = int(n),int(s)
    flag = 0
    l = list(map(int,input().split()))

    for z in range(len(l)):
        sum1=0
        for j in range(z,len(l)):
            sum1=sum1+l[j]
            if sum1>s:
                break
            if sum1==s:
                print(z+1,j+1)
                flag = 1
                break
        if flag == 1:
            break;

    if flag == 0:
        print("-1")
